from __future__ import unicode_literals, print_function
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet

from . import mixins as bulk_mixins


__all__ = [
    'BulkCreateAPIView',
    'BulkDestroyAPIView',
    'BulkModelViewSet',
    'BulkUpdateAPIView',
    'ListBulkCreateAPIView',
    'ListBulkCreateDestroyAPIView',
    'ListBulkCreateUpdateAPIView',
    'ListBulkCreateUpdateDestroyAPIView',
    'ListCreateBulkUpdateAPIView',
    'ListCreateBulkUpdateDestroyAPIView',
]


# ################################################## #
# Concrete view classes that provide method handlers #
# by composing the mixin classes with the base view. #
# ################################################## #

class BulkCreateAPIView(bulk_mixins.BulkCreateModelMixin,
                        GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BulkUpdateAPIView(bulk_mixins.BulkUpdateModelMixin,
                        GenericAPIView):
    def put(self, request, *args, **kwargs):
        return self.bulk_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_bulk_update(request, *args, **kwargs)


class BulkDestroyAPIView(bulk_mixins.BulkDestroyModelMixin,
                         GenericAPIView):
    def delete(self, request, *args, **kwargs):
        return self.bulk_destroy(request, *args, **kwargs)


class ListBulkCreateAPIView(mixins.ListModelMixin,
                            bulk_mixins.BulkCreateModelMixin,
                            GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListCreateBulkUpdateAPIView(mixins.ListModelMixin,
                                  mixins.CreateModelMixin,
                                  bulk_mixins.BulkUpdateModelMixin,
                                  GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.bulk_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_bulk_update(request, *args, **kwargs)


class ListCreateBulkUpdateDestroyAPIView(mixins.ListModelMixin,
                                         mixins.CreateModelMixin,
                                         bulk_mixins.BulkUpdateModelMixin,
                                         bulk_mixins.BulkDestroyModelMixin,
                                         GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.bulk_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_bulk_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.bulk_destroy(request, *args, **kwargs)


class ListBulkCreateUpdateAPIView(mixins.ListModelMixin,
                                  bulk_mixins.BulkCreateModelMixin,
                                  bulk_mixins.BulkUpdateModelMixin,
                                  GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.bulk_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_bulk_update(request, *args, **kwargs)


class ListBulkCreateDestroyAPIView(mixins.ListModelMixin,
                                   bulk_mixins.BulkCreateModelMixin,
                                   bulk_mixins.BulkDestroyModelMixin,
                                   GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.bulk_destroy(request, *args, **kwargs)


class ListBulkCreateUpdateDestroyAPIView(mixins.ListModelMixin,
                                         bulk_mixins.BulkCreateModelMixin,
                                         bulk_mixins.BulkUpdateModelMixin,
                                         bulk_mixins.BulkDestroyModelMixin,
                                         GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.bulk_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_bulk_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.bulk_destroy(request, *args, **kwargs)


# ########################################################## #
# Concrete viewset classes that provide method handlers      #
# by composing the bulk mixin classes with the base viewset. #
# ########################################################## #

class BulkModelViewSet(bulk_mixins.BulkCreateModelMixin,
                       bulk_mixins.BulkUpdateModelMixin,
                       bulk_mixins.BulkDestroyModelMixin,
                       ModelViewSet):
    pass
