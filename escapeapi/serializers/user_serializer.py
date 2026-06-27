from rest_framework import serializers
from escapeapi.models import User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_image', 'is_admin', 'created_at']

        