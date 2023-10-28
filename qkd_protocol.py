
import random

class QKDProtocol:
    def __init__(self):
        self.shared_key = None

    def generate_shared_key(self, key_length):
        self.shared_key = [random.choice([0, 1]) for _ in range(key_length)]

    def encrypt_message(self, message):
        encrypted_message = []
        for i in range(len(message)):
            encrypted_message.append(message[i] ^ self.shared_key[i % len(self.shared_key)])
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = []
        for i in range(len(encrypted_message)):
            decrypted_message.append(encrypted_message[i] ^ self.shared_key[i % len(self.shared_key)])
        return decrypted_message
