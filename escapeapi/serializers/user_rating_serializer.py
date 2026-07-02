from rest_framework import serializers
from escapeapi.models import UserRating

class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = ['id', 'user', 'game', 'fun', 'design', 'difficulty']