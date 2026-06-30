from django.db import models
from .game import Game

class GameImage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="images")
    image_path = models.CharField(max_length=500)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.game.title} - {self.image_path}"