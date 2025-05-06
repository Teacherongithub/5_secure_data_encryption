import hashlib
from cryptography.fernet import Fernet

# Generate a single encryption key
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()
