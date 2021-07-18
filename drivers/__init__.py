from core import commands

from drivers import (
    repos,
    adapters
)

send_message = commands.SendMessageCommand(
    message_repo=repos.message_repo,
    address_validator=adapters.address_validator,
    message_receipt_sender=adapters.message_receipt_sender
)