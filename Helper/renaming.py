# Function to rename image and label files in a folder with a base name.

import os


def rename_files(image_folder, label_folder, base_name):
    """
    Rename files in the specified image and label folders with a given base name.

    This function renames all files in the `image_folder` and `label_folder` by appending
    a sequential number to the `base_name` provided. The renaming is done in-place.

    Parameters:
    image_folder (str): The path to the folder containing image files to be renamed.
    label_folder (str): The path to the folder containing label files to be renamed.
    base_name (str): The base name to use for renaming the files.

    Returns:
    None
    """

    # Rename images
    for count, filename in enumerate(os.listdir(image_folder), start=1):
        file_extension = os.path.splitext(filename)[1]
        new_name = f"{base_name}_{count}{file_extension}"
        os.rename(
            os.path.join(image_folder, filename), os.path.join(image_folder, new_name)
        )

    # Rename labels
    for count, filename in enumerate(os.listdir(label_folder), start=1):
        file_extension = os.path.splitext(filename)[1]
        new_name = f"{base_name}_{count}{file_extension}"
        os.rename(
            os.path.join(label_folder, filename), os.path.join(label_folder, new_name)
        )
    print("COMPLETED RE-NAMING")


# Example usage
image_folder = "-----"
label_folder = "----"
base_name = "------"  # MY ID
rename_files(image_folder, label_folder, base_name)
