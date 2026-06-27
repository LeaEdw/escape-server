from rest_framework import viewsets
from escapeapi.models import Game
from escapeapi.serializers import GameSerializer
from escapeapi.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    