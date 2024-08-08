from rest_framework.permissions import IsAuthenticated
from ..permissions import IsAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet
from shop.api.v1.serializers import CommentSerializer
from shop.models import Comment


class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = CommentSerializer


    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Comment.objects.all()
        else:
            return Comment.objects.filter(is_published=True)
