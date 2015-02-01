from __future__ import unicode_literals, print_function
import copy
from rest_framework.routers import DefaultRouter, SimpleRouter


__all__ = [
    'BulkRouter',
]


class BulkRouter(DefaultRouter):
    """
    Map http methods to actions defined on the bulk mixins.
    """
    routes = copy.deepcopy(SimpleRouter.routes)
    routes[0].mapping.update({
        'put': 'bulk_update',
        'patch': 'partial_bulk_update',
        'delete': 'bulk_destroy',
    })
