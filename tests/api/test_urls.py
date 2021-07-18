from django.test import TestCase
from django.urls import reverse, resolve
from api import views

class TestUrls(TestCase):

    def test_messages_url(self):
        url = reverse("api:messages")
        self.assertEqual(resolve(url).func, views.messages.list)