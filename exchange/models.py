from django.db import models


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    seats = models.CharField(max_length=50)
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.university
