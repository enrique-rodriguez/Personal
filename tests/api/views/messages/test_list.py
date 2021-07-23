from app import models
from unittest.mock import Mock, patch
from django.urls import reverse
from assertpy import assert_that
from rest_framework import status
from rest_framework.test import APITestCase
from core.exceptions import InvalidMessageError


@patch('api.utils.captcha.requests')
class TestMessagesListView(APITestCase):

    def setUp(self):
        self.format = "json"
        self.url = reverse('api:messages')
    
    def get_post_data(self, **kwargs):
        data = self.get_default_data()
        data.update(kwargs)
        return data
    
    def get_default_data(self):
        return {
            "name": "First Last",
            "subject": "Subject",
            "body": "This is a simple message",
            "address": "my@address.com"
        }

    def test_post_message(self, requests):
        data = self.get_post_data()
        response = self.client.post(self.url, data, format=self.format)
        assert_that(response.status_code).is_equal_to(status.HTTP_201_CREATED)
        assert_that(models.MessageModel.objects.get().body).is_equal_to(data.get("body"))
    
    def test_post_message_with_empty_body_gives_error(self, requests):
        data = self.get_post_data(body='')
        response = self.client.post(self.url, data, format=self.format)
        assert_that(response.status_code).is_equal_to(status.HTTP_400_BAD_REQUEST)
        assert_that(response.data.get('error')).is_equal_to(InvalidMessageError.EMPTY_BODY)
    
    def test_post_message_with_empty_subject_gives_error(self, requests):
        data = self.get_post_data(subject='')
        response = self.client.post(self.url, data, format=self.format)
        assert_that(response.status_code).is_equal_to(status.HTTP_400_BAD_REQUEST)
        assert_that(response.data.get('error')).is_equal_to(InvalidMessageError.EMPTY_SUBJECT)
    
    def test_post_message_with_empty_name_gives_error(self, requests):
        data = self.get_post_data(name='')
        response = self.client.post(self.url, data, format=self.format)
        assert_that(response.status_code).is_equal_to(status.HTTP_400_BAD_REQUEST)
        assert_that(response.data.get('error')).is_equal_to(InvalidMessageError.EMPTY_NAME)

    def test_post_message_with_invalid_email_gives_error(self, requests):
        data = self.get_post_data(address='invalidemail')
        response = self.client.post(self.url, data, format=self.format)
        assert_that(response.status_code).is_equal_to(status.HTTP_400_BAD_REQUEST)
        assert_that(response.data.get('error')).is_equal_to(InvalidMessageError.ADDRESS)
    
    def test_post_message_body_too_short(self, requests):
        data = self.get_post_data(body='short message')
        response = self.client.post(self.url, data, format=self.format)
        assert_that(response.status_code).is_equal_to(status.HTTP_400_BAD_REQUEST)
        assert_that(response.data.get('error')).is_equal_to(InvalidMessageError.SHORT)
    
    def test_failed_captcha_challenge(self, requests):
        requests.post.return_value = Mock(json=Mock(return_value={"success": False}))
        data = self.get_post_data()
        response = self.client.post(self.url, data, format=self.format)
        assert_that(response.status_code).is_equal_to(status.HTTP_400_BAD_REQUEST)
        assert_that(response.data.get('error')).is_equal_to("captcha")
