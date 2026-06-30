from rest_framework import serializers
from escapeapi.models import Reaction


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ["id", "name", "icon"]
