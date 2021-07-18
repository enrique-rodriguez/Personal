from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from assertpy import assert_that
from app import models


class TestMessagesListView(APITestCase):
    
    def get_post_data(self, **kwargs):
        data = {
            "name": "First Last",
            "subject": "Subject",
            "body": "This is a simple message",
            "address": "my@address.com"
        }
        data.update(kwargs)
        return data

    def test_post_message(self):
        url = reverse("api:messages")
        data = self.get_post_data()
        response = self.client.post(url, data, format="json")
        assert_that(response.status_code).is_equal_to(status.HTTP_201_CREATED)
        assert_that(models.MessageModel.objects.get().body).is_equal_to("This is a simple message")
    
    def test_post_message_with_empty_body_gives_error(self):
        url = reverse("api:messages")
        data = self.get_post_data(body='')
        response = self.client.post(url, data, format="json")
        assert_that(response.status_code).is_equal_to(status.HTTP_400_BAD_REQUEST)
    
    def test_post_message_with_empty_subject_gives_error(self):
        url = reverse("api:messages")
        data = self.get_post_data(subject='')
        response = self.client.post(url, data, format="json")
        assert_that(response.status_code).is_equal_to(status.HTTP_400_BAD_REQUEST)
    
    def test_post_message_with_empty_name_gives_error(self):
        url = reverse("api:messages")
        data = self.get_post_data(name='')
        response = self.client.post(url, data, format="json")
        assert_that(response.status_code).is_equal_to(status.HTTP_400_BAD_REQUEST)
    
    def test_post_message_with_invalid_email_gives_error(self):
        url = reverse("api:messages")
        data = self.get_post_data(address='invalidemail')
        response = self.client.post(url, data, format="json")
        assert_that(response.status_code).is_equal_to(status.HTTP_400_BAD_REQUEST)