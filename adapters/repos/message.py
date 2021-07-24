import datetime
from app.models import MessageModel
from adapters.utils.repo import DjangoRepo


class MessageRepo(DjangoRepo):
    model = MessageModel

    def fetch_messages_from(self, address, date=None):
        date = date or datetime.date.today()
        return self.model.objects.filter(address=address, created__date=date).values()