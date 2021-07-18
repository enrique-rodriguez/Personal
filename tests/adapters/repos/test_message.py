from django.test import TestCase
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