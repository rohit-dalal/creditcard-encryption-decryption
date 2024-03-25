from os.path import exists

def store_in_cloud(file_path, text):
    try:
        if not exists(file_path):
            with open(file_path, 'w') as file:
                file.write(str(text))
                print(f"Credit card number successfully written to {file_path}.")
        else:
            with open(file_path, 'a') as file:
                file.write(str(text)+'\n')
                print(f"Credit card number successfully written.")

    except Exception as e:
        print(f"An error occurred while writing to {file_path}: {e}.")

