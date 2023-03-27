# Image Size Updater

This Python script is used to update the names of image files in a folder by adding their width and height dimensions to the file name. It reads the image files in the specified folder and gets their dimensions, and then renames them with the new name containing the dimensions.
for example: a file name "Green Car.jpg" will turn to "Green Car_4500x5400.jpg"

## Requirements

-   Python 3.x

## Usage

1.  Copy the script to a Python file (e.g., `image_size_updater.py`).
2.  Open the script and modify the `folder_path` variable to the path of the folder containing the image files you want to update.
3.  Save the changes and run the script.

## Functionality

The script uses two functions to get the dimensions of the image files and update their names:

### 1. get_image_size(file_path)

This function takes the path of an image file as input and returns its dimensions if it is a valid image file. It works as follows:

1.  It tries to open the file in binary mode and reads the first 24 bytes of the file.
2.  It uses the `imghdr.what()` function to determine the image format based on the header bytes.
3.  If the format is valid, it gets the file size and opens the file again.
4.  It reads the file data to find the image dimensions based on the format.
5.  It returns the dimensions as a tuple (width, height).

### 2. update_filename_with_size(file_path)

This function takes the path of an image file as input and updates its name by adding its dimensions to the file name. It works as follows:

1.  It gets the file name and extension from the path using the `os.path.splitext()` function.
2.  If the file extension is `.jpg`, `.jpeg`, or `.png`, it gets the dimensions using the `get_image_size()` function.
3.  If the dimensions are not `None`, it constructs the new file name with the dimensions and renames the file using the `os.rename()` function.
4.  If the dimensions are `None`, it skips the file.

### 3. update_folder(folder_path)

This function takes the path of a folder as input and iterates through its contents. If an item is a file, it calls the `update_filename_with_size()` function to update its name. If an item is a folder, it recursively calls itself to process its contents.

## Disclaimer

This script was created for educational purposes and is provided "as is" without warranty of any kind. The author is not responsible for any damage or loss caused by the use or misuse of this script. Use at your own risk.
