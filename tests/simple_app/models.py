from django.db import models


class SimpleModel (models.Model):
    contents = models.TextField()
