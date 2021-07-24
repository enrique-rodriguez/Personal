from django.test import TestCase
from unittest.mock import Mock
from assertpy import assert_that
from adapters.moderators import MessageModerator


class TestMessageModerator(TestCase):

    def setUp(self):
        self.message_repo = Mock(fetch_messages_from=Mock(return_value=[]))
        self.moderator = MessageModerator(message_repo=self.message_repo)

    def test_no_messages_not_under_send_limit(self):
        message = Mock()
        assert_that(self.moderator.is_under_send_limit(message)).is_true()
    
    def test_1_message_is_under_send_limit(self):
        message = Mock()
        self.moderator.send_limit = 1
        self.message_repo.fetch_messages_from.return_value = [Mock()]
        assert_that(self.moderator.is_under_send_limit(message)).is_false()

