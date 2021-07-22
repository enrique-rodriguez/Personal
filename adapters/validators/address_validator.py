import re


class EmailAddressValidator:
    pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
    
    def is_valid(self, email):
        return re.match(self.pattern, email)

address_validator = EmailAddressValidator()