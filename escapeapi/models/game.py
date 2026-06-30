"""Model for Escape Games"""

from django.db import models
from .location import Location

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=(50))
    active_status = models.BooleanField(default=True)
    number_of_players = models.IntegerField()
    age_recommendation = models.CharField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="games")


    def __str__(self):
        return self.title