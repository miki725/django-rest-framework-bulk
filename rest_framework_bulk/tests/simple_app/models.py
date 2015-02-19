from __future__ import unicode_literals, print_function
from django.db import models


class SimpleModel(models.Model):
    number = models.IntegerField()
    contents = models.CharField(max_length=16)


class UniqueTogetherModel(models.Model):
    foo = models.IntegerField()
    bar = models.IntegerField()

    class Meta(object):
        unique_together = ('foo', 'bar')
