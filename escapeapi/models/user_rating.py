"""Model for user ratings"""

from django.db import models
from .user import User
from .game import Game

class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ratings')
    fun = models.IntegerField()
    design = models.IntegerField()
    difficulty = models.IntegerField()

    class Meta:
        verbose_name = "userrating"
        verbose_name_plural = "userratings"

    def __str__(self):
        return f"{self.user} - {self.game}"