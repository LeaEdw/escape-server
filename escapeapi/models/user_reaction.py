"""Model for user reactions"""

from django.db import models

from .reaction import Reaction
from .comment import Comment
from .user import User

class UserReaction(models.Model):
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE, related_name='user_reactions')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reactions')

    def __str__(self):
        return f"{self.user} reacted to {self.comment}"