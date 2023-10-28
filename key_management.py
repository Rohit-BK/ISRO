
import key_generation
import key_distribution

class KeyManagement:
    def __init__(self):
        self.key_generation = key_generation.KeyGeneration()
        self.key_distribution = key_distribution.KeyDistribution()

    def generate_key(self):
        return self.key_generation.generate_key()

    def distribute_key(self, key):
        self.key_distribution.distribute_key(key)

    def encrypt_message(self, message):
        return self.key_distribution.encrypt_message(message)

    def decrypt_message(self, encrypted_message):
        return self.key_distribution.decrypt_message(encrypted_message)

