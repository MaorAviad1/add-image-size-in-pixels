import struct
import os
import imghdr


def get_image_size(file_path):
    try:
        with open(file_path, 'rb') as f:
            header = f.read(24)
            format = imghdr.what(None, header)
            if format:
                size = os.stat(file_path).st_size
                with open(file_path, 'rb') as img:
                    width, height = None, None
                    if format == 'jpeg':
                        # Skip the first two bytes (SOI marker)
                        img.seek(2)
                        while True:
                            marker, size = struct.unpack('>2sH', img.read(4))
                            if marker == b'\xc0\x00' or marker == b'\xc2\x00':
                                # Found the Start of Frame (SOF) marker with the image size
                                height, width = struct.unpack('>HH', img.read(4))
                                break
                            # Skip the bytes of the current segment
                            img.seek(size - 2, os.SEEK_CUR)
                    elif format == 'png':
                        # Skip the first 8 bytes (PNG signature)
                        img.seek(8)
                        while True:
                            # Read the length, type, and data of the next chunk
                            length, type = struct.unpack('>I4s', img.read(8))
                            if type == b'IHDR':
                                # Found the Image Header (IHDR) chunk with the image size
                                width, height = struct.unpack('>II', img.read(8))
                                break
                            # Skip the data of the current chunk
                            img.seek(length, os.SEEK_CUR)
                    if width is not None and height is not None:
                        return width, height
            else:
                print(f"Skipped file: {file_path} (not an image file)")
    except Exception as e:
        print(f"Error reading file: {file_path} ({e})")


def update_filename_with_size(file_path):
    file_name, file_ext = os.path.splitext(file_path)
    if file_ext.lower() in ['.jpg', '.jpeg', '.png']:
        size = get_image_size(file_path)
        if size is not None:
            new_file_name = f"{file_name}_{size[0]}x{size[1]}{file_ext}"
            os.rename(file_path, new_file_name)
            print(f"Updated file name: {new_file_name}")
        else:
            print(f"Skipped file: {file_path} (failed to get image size)")


def update_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            update_filename_with_size(item_path)
        elif os.path.isdir(item_path):
            update_folder(item_path)


folder_path = r'C:\AddImageSizes'
update_folder(folder_path)
