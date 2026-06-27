from rest_framework import serializers
from escapeapi.models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        field = ['id', 'title', 'description', 'difficulty', 'active_status', 'number_of_players', 'age_recommendation', 'location']