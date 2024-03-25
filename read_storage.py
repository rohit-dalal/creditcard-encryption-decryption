def print_storage_content(file_path):
    try:
        with open(file_path, 'r') as file:
            print("All Credit Cards:")
            return file.readlines()
        
    except Exception as e:
        print(f"An error occurred while reading from {file_path}: {e}")
