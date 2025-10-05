import os

def create_folder(folder_name):
    """Creates a new folder if it doesn't already exist."""
    try:
        # Create the directory
        os.makedirs(folder_name, exist_ok=True)
        # exist_ok=True prevents an error if the directory already exists
        print(f"Folder '{folder_name}' successfully created or already exists.")
    except OSError as e:
        print(f"Error creating folder '{folder_name}': {e}")

# Example usage:
new_folder = "C:\\Bhushan\\Personal"
create_folder(new_folder)