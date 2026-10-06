from django.db import models
from django.utils import timezone


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=200)
    country = models.CharField(max_length=100, blank=True)
    languages = models.CharField(max_length=200)
    seats = models.PositiveIntegerField()
    seats_is_maximum = models.BooleanField(default=False)
    deadline = models.DateField()
    description = models.TextField()

    @property
    def is_open(self):
        return self.deadline >= timezone.localdate()

    def __str__(self):
        return self.university