from django.db import models

class Person(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    votes = models.PositiveIntegerField()

    def __str__(self):
        return self.name

