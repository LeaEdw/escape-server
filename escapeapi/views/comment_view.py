from rest_framework import viewsets
from escapeapi.models import Comment
from escapeapi.serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer