from rest_framework_bulk import generics
from . import models


class SimpleBulkUpdateAPIView (generics.BulkUpdateAPIView):
    model = models.SimpleModel
