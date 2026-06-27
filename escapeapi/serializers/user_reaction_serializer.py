from rest_framework import serializers
from escapeapi.models import UserReaction

class UserReactionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserReaction
        fields = ['id', 'reaction', 'comment', 'user']