

class MessageModerator:

    def __init__(self, message_repo, send_limit=5):
        self.message_repo = message_repo
        self.send_limit = send_limit
    
    def is_under_send_limit(self, message):
        messages = self.message_repo.fetch_messages_from(message.address)
        return len(messages) < self.send_limit