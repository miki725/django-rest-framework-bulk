from __future__ import unicode_literals, print_function
from django.db import models


class SimpleModel(models.Model):
    number = models.IntegerField()
    contents = models.CharField(max_length=16)
