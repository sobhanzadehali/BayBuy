from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from ...models import CustomUser


class RegistrationApiView(generics.GenericAPIView):
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
