from __future__ import print_function, unicode_literals
from django.conf.urls import patterns, url, include
from rest_framework_bulk.routes import BulkRouter

from .views import SimpleViewSet


router = BulkRouter()
router.register('simple', SimpleViewSet, 'simple')

urlpatterns = patterns(
    '',

    url(r'^api/', include(router.urls, namespace='api')),
)
