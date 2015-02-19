from __future__ import print_function, unicode_literals
from django.conf.urls import patterns, url, include
from rest_framework_bulk.routes import BulkRouter

from .views import SimpleViewSet, UniqueTogetherViewSet


router = BulkRouter()
router.register('simple', SimpleViewSet, 'simple')
router.register('unique-together', UniqueTogetherViewSet, 'unique-together')

urlpatterns = patterns(
    '',

    url(r'^api/', include(router.urls, namespace='api')),
)
