from __future__ import unicode_literals, print_function
from rest_framework_bulk import generics

from . import models


class SimpleBulkAPIView(generics.ListBulkCreateUpdateDestroyAPIView):
    model = models.SimpleModel


class FilteredBulkAPIView(generics.ListBulkCreateUpdateDestroyAPIView):
    model = models.SimpleModel

    def filter_queryset(self, queryset):
        return queryset.filter(number__gt=5)
