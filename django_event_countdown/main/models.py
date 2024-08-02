from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name