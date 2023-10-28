
import encryption_utils

class Message:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.encrypted = False

    def encrypt(self, encryption_key):
        if not self.encrypted:
            self.body = encryption_utils.encrypt(self.body, encryption_key)
            self.encrypted = True

    def decrypt(self, decryption_key):
        if self.encrypted:
            self.body = encryption_utils.decrypt(self.body, decryption_key)
            self.encrypted = False

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n\n{self.body}"

