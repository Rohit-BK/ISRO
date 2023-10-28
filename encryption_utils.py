import random

def generate_symmetric_key(length):
    """
    Generates a symmetric key of the specified length.
    """
    key = ""
    for _ in range(length):
        key += random.choice("0123456789abcdef")
    return key

def encrypt_message(message, key):
    """
    Encrypts the given message using the provided key.
    """
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(ord(char) ^ int(key, 16))
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """
    Decrypts the given encrypted message using the provided key.
    """
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr(ord(char) ^ int(key, 16))
    return decrypted_message