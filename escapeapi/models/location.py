"""Model for Locations"""

from django.db import models

class Location(models.Model):
    city = models.CharField(max_length=255)
    area_location = models.CharField(max_length=255)

def __str__(self):
    return f"{self.city} - {self.area_location}"