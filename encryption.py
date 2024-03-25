from cryptography.fernet import Fernet, InvalidToken

def encrypt_data(data, key):
    try:
        # Initialize Fernet with the provided key
        f = Fernet(key)
        
        # Encrypt the data
        encrypted_data = f.encrypt(data.encode())
        
        return encrypted_data
    except Exception as e:
        print("An error occurred during encryption:", e)