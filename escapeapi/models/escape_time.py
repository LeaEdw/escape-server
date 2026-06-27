"""Model for user escape times"""

from django.db import models
from .user import User
from .game import Game

class EscapeTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='escapetimes')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='escapetimes')
    approval_status = models.BooleanField(default=True)
    escape_time = models.DurationField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.game} - {self.escape_time}"