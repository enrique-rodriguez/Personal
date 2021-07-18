

class InvalidMessageError(Exception):
    SHORT = "short"
    ADDRESS = "address"
    EMPTY_BODY = "empty"
    EMPTY_SUBJECT = "empty subject"
    EMPTY_NAME = "empty name"

    def __init__(self, reason, *args, **kwargs):
        self.reason = reason
        super().__init__(*args, **kwargs)
    
    @classmethod
    def empty_body(cls):
        return cls(cls.EMPTY_BODY, "Message body must not be empty.")
    
    @classmethod
    def empty_subject(cls):
        return cls(cls.EMPTY_SUBJECT, "Message subject must not be empty.")

    @classmethod
    def empty_name(cls):
        return cls(cls.EMPTY_NAME, "Sender name must not be empty.")

    @classmethod
    def short(cls, min_length):
        return cls(cls.SHORT, f"Message body must be atleast {min_length} characters long.")
    
    @classmethod
    def address(cls, address):
        return cls(cls.ADDRESS, f"The address '{address}' is not a valid address.")