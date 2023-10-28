
import random

class QKDService:
    def __init__(self):
        self.shared_key = None

    def generate_key(self, length):
        key = ""
        for _ in range(length):
            key += random.choice(["0", "1"])
        return key

    def distribute_key(self, key):
        self.shared_key = key

    def encrypt_message(self, message):
        encrypted_message = ""
        for i in range(len(message)):
            encrypted_message += chr(ord(message[i]) ^ int(self.shared_key[i % len(self.shared_key)]))
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        for i in range(len(encrypted_message)):
            decrypted_message += chr(ord(encrypted_message[i]) ^ int(self.shared_key[i % len(self.shared_key)]))
        return decrypted_message
