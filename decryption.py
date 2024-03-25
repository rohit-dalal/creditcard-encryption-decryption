from cryptography.fernet import Fernet, InvalidToken

def decrypt_data(encrypted_data, key):
    try:
        # Initialize Fernet with the provided key
        f = Fernet(key)
        
        # Decrypt the data
        decrypted_data = f.decrypt(encrypted_data)
        
        return decrypted_data.decode()
    
    except InvalidToken:
        print("Invalid token. Decryption failed: The token provided is invalid or corrupted.")
    except Exception as e:
        print("An error occurred during decryption:", e)

