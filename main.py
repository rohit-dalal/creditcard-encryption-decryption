# main.py
from authentication import authenticate_user, check_access
from encryption import encrypt_data
from cloud_storage import store_in_cloud
from decryption import decrypt_data
from read_storage import print_storage_content

storage_file='storage.key'

def secret_key():
    return b'jTnjuRiLBQ-nIS6Ro2nnXU1eHAbK5n6YH9Hus_Va33Q='


def main():
    # Example usage of modules
    username = input("Enter username: ")
    password = input("Enter password: ")

    if authenticate_user(username, password):
        print("Authentication successful.")
        user_role = "admin"  # Replace with actual user role retrieval logic

        if check_access(user_role, "admin"):
            credit_card_number = input("Enter credit card number: ")

            # Encryption
            key = secret_key()
            encrypted_data = encrypt_data(credit_card_number, key)

            # save to cloud
            store_in_cloud(storage_file, encrypted_data)

            # show credit cards
            print('-'*65)
            for bytes in print_storage_content(storage_file):
                print(bytes.strip())
                #decrypted_data = decrypt_data(bytes.strip(), key)
                #print(decrypted_data)
                #print(bytes.strip())
            print('-'*65)
        else:
            print("Access denied.")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()
