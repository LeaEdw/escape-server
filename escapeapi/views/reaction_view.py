from rest_framework import viewsets
from escapeapi.models import Reaction
from escapeapi.serializers import ReactionSerializer
from escapeapi.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class ReactionViewSet(viewsets.ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]