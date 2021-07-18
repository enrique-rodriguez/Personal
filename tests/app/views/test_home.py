from app import models
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class TestHomeView(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(username="username", password="password")
        models.ProfileModel.objects.create(user=self.user)

    def test_get(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')
        self.assertContext(response)
    
    def assertContext(self, response):
        self.assertIn("profile", response.context)
        self.assertIn("social_links", response.context)