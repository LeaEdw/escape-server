from rest_framework import serializers
from escapeapi.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = ['id', 'user', 'game', 'title', 'comment_body', 'created_at']