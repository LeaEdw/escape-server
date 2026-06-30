""""Model for reactions"""

from django.db import models

class Reaction(models.Model):
    icon = models.ImageField(upload_to='reactions/')
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return f"Reaction {self.icon}"