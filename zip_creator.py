import zipfile  # Importing the zipfile module for zip file operations
import pathlib  # Importing the pathlib module for handling paths


def make_archive(filepaths, dest_directory):
    """
    Create a zip archive containing specified files.

    Args:
    - filepaths (list): List of file paths to be included in the archive.
    - dest_directory (str): Destination directory where the archive will be created.

    Returns:
    - None

    """
    # Create a Path object for the destination zip file
    dest_path = pathlib.Path(dest_directory, "compressed.zip")

    # Open a new ZipFile object for writing to the destination path
    with zipfile.ZipFile(dest_path, 'w') as archive:
        # Iterate over each file path in the list
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)  # Convert the file path to a Path object
            archive.write(filepath, arcname=filepath.name)  # Add the file to the archive with its base name

        # Print a message after successful completion (can be replaced with logging or removed in production)
        print("Archive created successfully.")

# Example usage if running as a standalone script
# if __name__ == "__main__":
#     make_archive(filepaths=["another_file.txt", "file_to_compress.txt"],
#                  dest_directory="output_files")
