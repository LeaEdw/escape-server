from rest_framework import serializers
from escapeapi.models import Location

class LocationSerializer(serializers.ModelSerializer):
     class Meta: 
          model = Location
          fields = ['id', 'city', 'area_location'
          ]