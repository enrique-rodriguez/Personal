from unittest import TestCase
from unittest.mock import Mock
from assertpy import assert_that
from core.commands import SendMessageCommand
from core.exceptions import InvalidMessageError


class TestSendMessageCommand(TestCase):

    def setUp(self):
        self.message_repo = Mock()
        self.address_validator = Mock()
        self.message_receipt_sender = Mock()
        self.send_message = self.get_command()
    
    def get_command(self):
        return SendMessageCommand(
            message_repo=self.message_repo,
            address_validator=self.address_validator,
            message_receipt_sender=self.message_receipt_sender
        )
    
    def get_request(self, **kwargs):
        data = self.get_default_data()
        data.update(kwargs)
        return data
    
    def get_default_data(self):
        return dict(
            name='First Last',
            address='address', 
            subject='subject', 
            body='this is the message body.'
        )
    
    def assertInvalidMessage(self, request, reason):
        try:
            self.send_message(request)
        except InvalidMessageError as error:
            assert_that(error.reason).is_equal_to(reason)

    def test_empty_message_body_raises_invalid_message_error(self):
        request = self.get_request(body='')
        self.assertInvalidMessage(request, InvalidMessageError.EMPTY_BODY)
    
    def test_empty_name_raises_invalid_message_error(self):
        request = self.get_request(name='')
        self.assertInvalidMessage(request, InvalidMessageError.EMPTY_NAME)
    
    def test_empty_message_subject_raises_invalid_message_error(self):
        request = self.get_request(subject='')
        self.assertInvalidMessage(request, InvalidMessageError.EMPTY_SUBJECT)
    
    def test_invalid_address_raises_invalid_message_error(self):
        self.address_validator.is_valid.return_value = False
        request = self.get_request(address='invalid_address')
        self.assertInvalidMessage(request, InvalidMessageError.ADDRESS)
    
    def test_message_body_to_small_raises_invalid_message(self):
        request = self.get_request(body='short message')
        self.assertInvalidMessage(request, InvalidMessageError.SHORT)
    
    def test_message_saved(self):
        request = self.get_request()
        self.send_message(request)
        self.message_repo.save.assert_called()

    def test_message_receipt_sent(self):
        request = self.get_request()
        self.send_message(request)
        self.message_receipt_sender.send.assert_called()
    
    def test_returns_dictionary_response(self):
        request = self.get_request()
        response = self.send_message(request)
        assert_that(response).is_type_of(dict)