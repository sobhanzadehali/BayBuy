import json

from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings

from django.apps import apps

from .serializers import ZibalpaySerializer


def find_model(app_model_string):
    """
    takes string like 'shop.Order' and returns order model
    """

    model_string = app_model_string
    dot_index = model_string.index('.')
    return apps.get_model(model_string[:dot_index], model_string[dot_index + 1:])


Order = find_model(settings.ORDER_MODEL)


@api_view(['GET'])
@permission_classes(IsAuthenticated, )
def send_pay_request(request, order_id):
    """
    this view is for sending pay request to zibal and it shows a payment link if everything was good.
    :param request:
    :param order_id:
    """
    phone = request.user.phone if request.user.phone else request.user.mobile

    try:
        order = Order.object.get(id=order_id)
        if order.buyer_id is not request.user:
            raise PermissionError('You are not authorized to pay this order order')
    except Order.DoesNotExist:
        raise NotFound('Order not found')
    data = {
        'merchant': settings.ZIBALPAY_MERCHANT,
        'order_id': order_id,
        'amount': order.calculate_total_fee,
        'callbackUrl': settings.ZIBALPAY_CALLBACK_URL,
        'mobile': phone,
    }
    response = requests.post('https://gateway.zibal.ir/v1/request', data=data,
                             headers={'Content-Type': 'application/json'})
    response = json.loads(response.content)
    if response.result == 100:
        data = {
            "payLink": f"https://gateway.zibal.ir/start/{response['trackId']}"
        }
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        return Response(data={'data': 'something wen\'t wrong!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@throttle_classes([AnonRateThrottle, ])
def callback_view(request):
    """
    this view is used by zibal to send get request for notifying a payment has been
    created. also hackers can try sending request to this endpoint but it will be verified with zibal verification
    api.
    it has a throttle policy so a non user(per IP) only can send 200 requests a day.
    :param request:
    :return: Respone object
    """
    trackId = request.GET.get('trackId')
    orderId = request.GET.get('orderId')
    payStatus = request.GET.get('status')
    success = request.GET.get('success')
    if success == 1:

        data = {
            'merchant': settings.ZIBALPAY_MERCHANT,
            'trackId': trackId,
        }
        response = requests.post('https://gateway.zibal.ir/v1/verify',
                                 data=data, headers={'Content-Type': 'application/json'})
        serilizer_class = ZibalpaySerializer(data=response.json())
        if serilizer_class.is_valid():
            if serilizer_class.validated_data['trackId'] == trackId and serilizer_class.validated_data['result'] == 100:
                serilizer_class.save()
                order_obj = Order.object.get(id=serilizer_class.validated_data['orderId'])
                order_obj.pay(serilizer_class.validated_data['paidAt'])

            return Response(serilizer_class.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)
