from django.db import models


class Plop(models.Model):
    name = models.CharField(max_length=32)


class Child(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey(Plop, related_name='children')
