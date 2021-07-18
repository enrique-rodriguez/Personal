from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from assertpy import assert_that


class TestMessagesListView(APITestCase):

    def test_post_message(self):
        url = reverse("api:messages")
        data = {
            "name": "First Last",
            "subject": "Subject",
            "body": "This is a simple message",
            "address": "my@address.com"
        }
        response = self.client.post(url, data, format="json")
        assert_that(response.status_code).is_equal_to(status.HTTP_201_CREATED)