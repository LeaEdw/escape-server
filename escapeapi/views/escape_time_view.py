from rest_framework import viewsets
from escapeapi.models import EscapeTime
from escapeapi.serializers import EscapeTimeSerializer

class EscapeTimeViewSet(viewsets.ModelViewSet):
    queryset = EscapeTime.objects.all()
    serializer_class = EscapeTimeSerializer