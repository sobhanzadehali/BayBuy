from rest_framework import serializers
from shop.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

