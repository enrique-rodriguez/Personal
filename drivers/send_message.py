from core import commands

from adapters import (
    repos,
    validators,
    notifications,
    moderators
)

def send_message(data, send_limit):
    return commands.SendMessageCommand(
        message_repo=repos.message_repo,
        address_validator=validators.address_validator,
        moderator=moderators.get_message_moderator(send_limit),
        message_receipt_sender=notifications.message_receipt_sender,
    )(data)