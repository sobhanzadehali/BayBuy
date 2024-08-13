from rest_framework import views, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer, SellerSerializer
from ...models import CustomUser, SellerInfo


class RegistrationApiView(generics.GenericAPIView):
    """
    takes phone number and password. validates phone number and password.
    if everything was ok, creates a new user and returns its data.
    """
    serializer_class = RegistrationSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        if self.queryset.filter(phone=phone).exists():
            return Response({'error': 'Phone already registered'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class TokenLogoutView(views.APIView):
    """
    logs out a user and returns nothing.
    basically it removes created token.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellerInfoApiView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SellerSerializer
    queryset = SellerInfo.objects.all()

    def get(self, request):
        """
        use this view to get seller's info
        get empty form to send identification docs, if not sent before
        and will show seller identification data
        """

        seller_info = SellerInfo.objects.filter(seller_id=request.user)
        serializer = self.serializer_class(seller_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        use this view to send identification docs, if not sent before
        """
        if request.user.is_seller:
            data = {'data': 'you are already seller'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer_class(data={
            'seller_id': request.user,
            'video': request.FILES['video'],
            'id_card': request.FILES['card_id'],
            'id_number': request.data['id_number'],
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
