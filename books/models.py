from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.IntegerField()

    def __str__(self):
        return '<Book: %s>' %(self.name)
