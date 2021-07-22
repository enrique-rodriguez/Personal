from app.models import MessageModel
from adapters.utils.repo import DjangoRepo


class MessageRepo(DjangoRepo):
    model = MessageModel
