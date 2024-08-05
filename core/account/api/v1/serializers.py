from rest_framework import serializers

from account.models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):

        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                'Passwords must match'
            )
        else:
            return data

    def validate_phone(self, data):
        if data[:2] != '09':
            raise serializers.ValidationError(
                'Phone numbers must begin with "09"'
            )
        if len(data) != 11:
            raise serializers.ValidationError(
                'phone number is invalid'
            )
        else:
            return data

    def create(self, validated_data):

        user = CustomUser.objects.create_user(phone=validated_data['phone'], password=validated_data['password1'])
        return user

    class Meta:
        model = CustomUser
        fields = ('phone', 'password1', 'password2')
