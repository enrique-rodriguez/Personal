from core import commands

from adapters import (
    repos,
    validators,
    notifications
)

def send_message(*args, **kwargs):
    return commands.SendMessageCommand(
        message_repo=repos.message_repo,
        address_validator=validators.address_validator,
        message_receipt_sender=notifications.message_receipt_sender
    )(*args, **kwargs)