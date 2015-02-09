from __future__ import unicode_literals, print_function
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response


__all__ = [
    'BulkCreateModelMixin',
    'BulkDestroyModelMixin',
    'BulkUpdateModelMixin',
]


class BulkCreateModelMixin(CreateModelMixin):
    """
    Either create a single or many model instances in bulk by using the
    Serializers ``many=True`` ability from Django REST >= 2.2.5.

    .. note::
        This mixin uses the same method to create model instances
        as ``CreateModelMixin`` because both non-bulk and bulk
        requests will use ``POST`` request method.
    """

    def create(self, request, *args, **kwargs):
        bulk = isinstance(request.DATA, list)

        if not bulk:
            return super(BulkCreateModelMixin, self).create(request, *args, **kwargs)

        else:
            serializer = self.get_serializer(data=request.DATA, many=True)
            if serializer.is_valid():
                for obj in serializer.object:
                    self.pre_save(obj)
                self.object = serializer.save(force_insert=True)
                for obj in self.object:
                    self.post_save(obj, created=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BulkUpdateModelMixin(object):
    """
    Update model instances in bulk by using the Serializers
    ``many=True`` ability from Django REST >= 2.2.5.
    """

    def get_object(self, queryset=None):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        if any((lookup_url_kwarg in self.kwargs,
                self.pk_url_kwarg in self.kwargs,
                self.slug_url_kwarg in self.kwargs)):
            return super(BulkUpdateModelMixin, self).get_object(queryset)

        # If the lookup_url_kwarg (or other deprecated variations)
        # are not present, get_object() is most likely called
        # as part of metadata() which by default simply checks
        # for object permissions and raises permission denied if necessary.
        # Here we don't need to check for general permissions
        # and can simply return None since general permissions
        # are checked in initial() which always gets executed
        # before any of the API actions (e.g. create, update, etc)
        return

    def bulk_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        # restrict the update to the filtered queryset
        serializer = self.get_serializer(self.filter_queryset(self.get_queryset()),
                                         data=request.DATA,
                                         many=True,
                                         partial=partial)

        if serializer.is_valid():
            try:
                for obj in serializer.object:
                    self.pre_save(obj)
            except ValidationError as err:
                # full_clean on model instances may be called in pre_save
                # so we have to handle eventual errors.
                return Response(err.message_dict, status=status.HTTP_400_BAD_REQUEST)
            self.object = serializer.save(force_update=True)
            for obj in self.object:
                self.post_save(obj, created=False)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_bulk_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.bulk_update(request, *args, **kwargs)


class BulkDestroyModelMixin(object):
    """
    Destroy model instances.
    """

    def allow_bulk_destroy(self, qs, filtered):
        """
        Hook to ensure that the bulk destroy should be allowed.

        By default this checks that the destroy is only applied to
        filtered querysets.
        """
        return qs is not filtered

    def bulk_destroy(self, request, *args, **kwargs):
        qs = self.get_queryset()
        filtered = self.filter_queryset(qs)
        if not self.allow_bulk_destroy(qs, filtered):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        for obj in filtered:
            self.pre_delete(obj)
            obj.delete()
            self.post_delete(obj)
        return Response(status=status.HTTP_204_NO_CONTENT)
