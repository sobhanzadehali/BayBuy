from rest_framework import serializers

from account.models import CustomUser, SellerInfo


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'fname', 'lname', ]


class SellerSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        id_number = attrs.get('id_number')
        if not id_number:
            raise serializers.ValidationError('id_number is required')
        control_code = id_number[-1]
        sumation = 0
        for i in range(len(id_number)):
            for j in range(len(id_number) - 1):
                sumation += int(id_number[-i]) * (j + 1)
        calculated_value = sumation % 11
        if calculated_value < 0 and calculated_value == control_code:
            return super().validate(attrs)
        if calculated_value > control_code:
            if calculated_value - 11 == control_code:
                return super().validate(attrs)
        else:
            raise serializers.ValidationError(
                "id_number is not valid. double check before trying again!"
            )

    class Meta:
        model = SellerInfo
        fields = '__all__'
