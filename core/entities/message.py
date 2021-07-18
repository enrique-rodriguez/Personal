from core.entities.entity import Entity
from core.exceptions import InvalidMessageError


class Message(Entity):
    MIN_MESSAGE_LEN = 20
    
    def __init__(self, name, address, subject, body, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if body == '':
            raise InvalidMessageError.empty_body()
        if name == '':
            raise InvalidMessageError.empty_name()
        if subject == '':
            raise InvalidMessageError.empty_subject()
        if len(body) < self.MIN_MESSAGE_LEN:
            raise InvalidMessageError.short(self.MIN_MESSAGE_LEN)
        self.body = body
        self.address = address