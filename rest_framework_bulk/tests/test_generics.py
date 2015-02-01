from __future__ import unicode_literals, print_function
import json
from django.test import TestCase
from django.test.client import RequestFactory
from rest_framework import status

from .simple_app.models import SimpleModel
from .simple_app.views import FilteredBulkAPIView, SimpleBulkAPIView


class TestBulkAPIView(TestCase):
    def setUp(self):
        super(TestBulkAPIView, self).setUp()
        self.view = SimpleBulkAPIView.as_view()
        self.request = RequestFactory()

    def test_get(self):
        """
        Test that GET request is successful on bulk view.
        """
        response = self.view(self.request.get(''))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_single(self):
        """
        Test that POST request with single resource only creates a single resource.
        """
        response = self.view(self.request.post(
            '',
            json.dumps({'contents': 'hello world', 'number': 1}),
            content_type='application/json',
        ))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SimpleModel.objects.count(), 1)
        self.assertEqual(SimpleModel.objects.get().contents, 'hello world')

    def test_post_bulk(self):
        """
        Test that POST request with multiple resources creates all posted resources.
        """
        response = self.view(self.request.post(
            '',
            json.dumps([
                {'contents': 'hello world', 'number': 1},
                {'contents': 'hello mars', 'number': 2},
            ]),
            content_type='application/json',
        ))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SimpleModel.objects.count(), 2)
        self.assertEqual(list(SimpleModel.objects.all().values_list('contents', flat=True)), [
            'hello world',
            'hello mars',
        ])

    def test_put(self):
        """
        Test that PUT request updates all submitted resources.
        """
        obj1 = SimpleModel.objects.create(contents='hello world', number=1)
        obj2 = SimpleModel.objects.create(contents='hello mars', number=2)

        response = self.view(self.request.put(
            '',
            json.dumps([
                {'contents': 'foo', 'number': 3, 'id': obj1.pk},
                {'contents': 'bar', 'number': 4, 'id': obj2.pk},
            ]),
            content_type='application/json',
        ))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SimpleModel.objects.count(), 2)
        self.assertEqual(
            list(SimpleModel.objects.all().values_list('id', 'contents', 'number')),
            [
                (obj1.pk, 'foo', 3),
                (obj2.pk, 'bar', 4),
            ]
        )

    def test_patch(self):
        """
        Test that PATCH request partially updates all submitted resources.
        """
        obj1 = SimpleModel.objects.create(contents='hello world', number=1)
        obj2 = SimpleModel.objects.create(contents='hello mars', number=2)

        response = self.view(self.request.patch(
            '',
            json.dumps([
                {'contents': 'foo', 'id': obj1.pk},
                {'contents': 'bar', 'id': obj2.pk},
            ]),
            content_type='application/json',
        ))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SimpleModel.objects.count(), 2)
        self.assertEqual(
            list(SimpleModel.objects.all().values_list('id', 'contents', 'number')),
            [
                (obj1.pk, 'foo', 1),
                (obj2.pk, 'bar', 2),
            ]
        )

    def test_delete_not_filtered(self):
        """
        Test that DELETE is not allowed when results are not filtered.
        """
        SimpleModel.objects.create(contents='hello world', number=1)
        SimpleModel.objects.create(contents='hello mars', number=10)

        response = self.view(self.request.delete(''))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_filtered(self):
        """
        Test that DELETE removes all filtered resources.
        """
        SimpleModel.objects.create(contents='hello world', number=1)
        SimpleModel.objects.create(contents='hello mars', number=10)

        response = FilteredBulkAPIView.as_view()(self.request.delete(''))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SimpleModel.objects.count(), 1)
        self.assertEqual(SimpleModel.objects.get().contents, 'hello world')

    def test_options(self):
        """
        Test that OPTIONS request is successful on bulk view.
        """
        response = self.view(self.request.options(''))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
