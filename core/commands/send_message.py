from core.utils import Command
from dataclasses import dataclass
from core.exceptions import InvalidMessageError, TooManyMessagesError


class SendMessageCommand(Command):

    @dataclass(frozen=True)
    class Request:
        name: str
        body: str
        subject: str
        address: str

    def __init__(self, moderator, message_repo, address_validator, message_receipt_sender):
        self.moderator = moderator
        self.message_repo = message_repo
        self.address_validator = address_validator
        self.message_receipt_sender = message_receipt_sender
        
    def execute(self, request):
        if not self.address_validator.is_valid(request.address):
            raise InvalidMessageError.address(request.address)
        message = self.make.message(**vars(request))
        if not self.moderator.is_under_send_limit(message):
            raise TooManyMessagesError
        self.message_repo.save(vars(message))
        message.id = self.message_repo.last_insert_id
        self.message_receipt_sender.send(message)
        return vars(message)
        