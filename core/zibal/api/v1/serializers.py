from rest_framework import serializers

from zibal.models import Zibalpay


class ZibalpaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Zibalpay
        fields = '__all__'
