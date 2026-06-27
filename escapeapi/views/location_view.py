from rest_framework import viewsets
from escapeapi.models import Location
from escapeapi.serializers import LocationSerializer
from escapeapi.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]