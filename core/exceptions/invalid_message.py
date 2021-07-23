

class InvalidMessageError(Exception):
    SHORT = "short"
    ADDRESS = "address"
    EMPTY_BODY = "empty"
    EMPTY_SUBJECT = "empty subject"
    EMPTY_NAME = "empty name"

    def __init__(self, reason, **kwargs):
        self.reason = reason
        self.kwargs = kwargs
    
    @classmethod
    def empty_body(cls):
        return cls(cls.EMPTY_BODY)
    
    @classmethod
    def empty_subject(cls):
        return cls(cls.EMPTY_SUBJECT)

    @classmethod
    def empty_name(cls):
        return cls(cls.EMPTY_NAME)

    @classmethod
    def short(cls, min_length):
        return cls(cls.SHORT, min_length=min_length)
    
    @classmethod
    def address(cls, address):
        return cls(cls.ADDRESS, address=address)