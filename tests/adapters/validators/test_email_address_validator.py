from unittest import TestCase
from assertpy import assert_that
from adapters.validators.address_validator import EmailAddressValidator

class TestEmailAddressValidator(TestCase):

    def setUp(self):
        self.validator = EmailAddressValidator()

    def test_valid_email_returns_true(self):
        is_valid = self.validator.is_valid("email@email.com")
        assert_that(is_valid).is_true()
    
    def test_invalid_email_returns_false(self):
        invalid = [
            "invalidemail.com",
            "invalidemail",
            "@email",
            "@email.com",
            "invalidemail@",
        ]

        for email in invalid:
            assert_that(self.validator.is_valid(email)).is_false()