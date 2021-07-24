from time import time
from django.test import TestCase
from datetime import datetime, date
from django.utils.timezone import make_aware
from assertpy import assert_that
from adapters.repos.message import MessageRepo

class TestMessageRepo(TestCase):

    def setUp(self):
        self.repo = MessageRepo()

    def test_empty_repo_has_no_messages(self):
        assert_that(self.repo.count()).is_equal_to(0)
        assert_that(self.repo.last_insert_id).is_none()

    def test_save_message(self):
        self.repo.save({
            "name": "First Last",
            "subject": "Subject",
            "body": "body",
            "address": "email@email.com"
        })
        assert_that(self.repo.count()).is_equal_to(1)
        assert_that(self.repo.last_insert_id).is_equal_to(1)
    
    def test_fetch_messages_from_sender_gives_empty_if_no_messages_found(self):
        assert_that(self.repo.fetch_messages_from('email@email.com')).is_empty()
    
    def test_fetch_messages_sender_gives_list_of_size_2(self):
        self.repo.save({
            "name": "First Last",
            "subject": "Message 1",
            "body": "Body 1",
            "address": "email@email.com"
        })
        self.repo.save({
            "name": "First Last",
            "subject": "Message 2",
            "body": "Body 2",
            "address": "email@email.com"
        })

        assert_that(self.repo.fetch_messages_from('email@email.com')).is_length(2)
    
    def test_fetch_messages_from_sender_from_date_gives_list_of_size_1(self):
        # Save message from 2012-12-12
        self.repo.save({
            "name": "First Last",
            "subject": "Message 1",
            "body": "Body 1",
            "address": "email@email.com",
            "created": make_aware(datetime(2012, 12, 12, 12, 12))
        })
        # Save message from 2012-12-13
        self.repo.save({
            "name": "First Last",
            "subject": "Message 2",
            "body": "Body 2",
            "address": "email@email.com",
            "created": make_aware(datetime(2012, 12, 13, 12, 12))
        })
        # Look for messages from 2012-12-12
        d = date(2012,12,12)
        assert_that(self.repo.fetch_messages_from('email@email.com', date=d)).is_length(1)