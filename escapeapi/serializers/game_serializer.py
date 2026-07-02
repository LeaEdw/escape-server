from rest_framework import serializers
from escapeapi.models import Game, GameImage


class GameImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameImage
        fields = ["id", "image_path", "is_primary"]


class GameSerializer(serializers.ModelSerializer):
    images = GameImageSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = [
            "id",
            "title",
            "description",
            "difficulty",
            "active_status",
            "number_of_players",
            "age_recommendation",
            "location",
            "images",
        ]
