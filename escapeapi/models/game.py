"""Model for Escape Games"""

from django.db import models
from .location import Location

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.IntegerField()
    active_status = models.BooleanField(default=True)
    number_of_players = models.IntegerField()
    age_recommendation = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="games")
    image_path = models.ImageField(
        upload_to="games",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
    )

    def __str__(self):
        return self.title