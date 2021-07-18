from django.test import TestCase
from django.urls import reverse, resolve
from app import views

class TestUrls(TestCase):
    
    def test_homepage_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)