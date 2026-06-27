from rest_framework import viewsets
from escapeapi.models import UserReaction
from escapeapi.serializers import UserReactionSerializer

class UserReactionViewSet(viewsets.ModelViewSet):
    queryset = UserReaction.objects.all()
    serializer_class = UserReactionSerializer