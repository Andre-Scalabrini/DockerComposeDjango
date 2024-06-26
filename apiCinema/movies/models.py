from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.title
