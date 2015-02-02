from __future__ import print_function, unicode_literals
from rest_framework.serializers import ModelSerializer

from .models import SimpleModel


class SimpleSerializer(ModelSerializer):
    class Meta(object):
        model = SimpleModel
