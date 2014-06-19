from django.test import TestCase
from django.test.client import RequestFactory
from simple_app.views import SimpleBulkUpdateAPIView


class TestBulkUpdateAPIView(TestCase):
    def test_OPTIONS_request(self):
        """
        OPTIONS requests must work for CORS requests. Test that OPTIONS
        requests aren't failing for simple cases.
        """
        view = SimpleBulkUpdateAPIView.as_view()
        request = RequestFactory().options('')
        response = view(request)

        self.assertEqual(response.status_code, 200)
