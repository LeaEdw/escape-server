""""Model for reactions"""

from django.db import models

class Reaction(models.Model):
    icon = models.ImageField(upload_to='reactions/')

    def __str__(self):
        return f"Reaction {self.id}"