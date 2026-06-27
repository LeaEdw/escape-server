"""Model for Comments"""

from django.db import models

from .user import User
from .game import Game

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=255)
    comment_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.title}"
