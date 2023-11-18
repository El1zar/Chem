from cryptography.fernet import Fernet
import base64

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(password.encode())
    return base64.urlsafe_b64encode(cipher_text).decode()

def decrypt_password(key, cipher_text):
    try:
        cipher_suite = Fernet(key)
        decrypted_password = cipher_suite.decrypt(base64.urlsafe_b64decode(cipher_text)).decode()
        return decrypted_password
    except Exception as e:
        return f"Помилка розшифрування: {e}"
