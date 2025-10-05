import os
import shutil


def organize_files_by_prefix(source_dir: str, target_dir: str, prefix: str):
    """
    Scans a source directory for files starting with a specific prefix
    and moves them into a designated target directory.

    Args:
        source_dir (str): The directory to search for files.
        target_dir (str): The destination directory for the matching files.
        prefix (str): The starting string files must match (case-sensitive).
    """

    # 1. Check if the source directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory not found at '{source_dir}'.")
        return

    # 2. Create the target directory if it doesn't exist
    try:
        # exist_ok=True prevents an error if the directory already exists
        os.makedirs(target_dir, exist_ok=True)
        print(f"Target directory '{target_dir}' is ready.")
    except OSError as e:
        print(f"Error creating target directory: {e}")
        return

    moved_count = 0

    # 3. Iterate through all items in the source directory
    print(f"\nScanning files in: {source_dir}...")
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Check if the item is a file AND starts with the required prefix
        if os.path.isfile(source_path) and filename.startswith(prefix):
            target_path = os.path.join(target_dir, filename)

            try:
                # 4. Move the file using shutil.move
                # shutil.move handles moving files even across different disk partitions.
                shutil.move(source_path, target_path)
                print(f"  [MOVED] '{filename}' to '{target_dir}'")
                moved_count += 1
            except Exception as e:
                print(f"  [ERROR] Failed to move '{filename}': {e}")

    print(f"\n--- Operation Complete ---")
    print(f"Successfully moved {moved_count} files starting with '{prefix}'.")
    if moved_count == 0:
        print(f"No files matching prefix '{prefix}' were found.")


# =================================================================
#                         DEMONSTRATION SETUP
# =================================================================

print("--- FILE ORGANIZER SETUP ---")

# Get Source Directory from user
SOURCE_FOLDER = input("Enter the source folder path (e.g., /home/user/downloads or 'inbox_to_sort'): ")

# Get Prefix from user
FILE_PREFIX = input("Enter the file prefix to search for (e.g., 'report_'): ")

# Get Target Directory from user (NEW INPUT)
TARGET_FOLDER = input("Enter the target folder name for the organized files: ")

print("---------------------------")
print(f"Source Folder set to: {SOURCE_FOLDER}")
print(f"Files starting with prefix: '{FILE_PREFIX}' will be moved.")
print(f"Target Folder set to: {TARGET_FOLDER}")
print("---------------------------")

# --- RUN THE FILE ORGANIZER ---
organize_files_by_prefix(
    source_dir=SOURCE_FOLDER,
    target_dir=TARGET_FOLDER,
    prefix=FILE_PREFIX
)
