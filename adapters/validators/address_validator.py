import re


class EmailAddressValidator:
    def is_valid(self, email):
        return re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email)

address_validator = EmailAddressValidator()