""""Model for reactions"""

from django.db import models

class Reaction(models.Model):
    icon = models.ImageField(upload_to='reactions/')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Reaction {self.icon}"