
import random

class KeyGeneration:
    def __init__(self):
        self.key_length = 128

    def generate_key(self):
        key = ""
        for _ in range(self.key_length):
            key += random.choice(["0", "1"])
        return key

