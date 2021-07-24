from .message import MessageModerator
from adapters import repos

def get_message_moderator(send_limit):
    return MessageModerator(
        message_repo=repos.message_repo,
        send_limit=send_limit
    )