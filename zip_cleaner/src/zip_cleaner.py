import os
import glob
import ctypes
from pathlib import Path
from send2trash import send2trash

def delete_extracted_zips(folder_path):
    zip_files = glob.glob(os.path.join(folder_path, "*.zip"))
    deleted = []

    for zip_file in zip_files:
        base_name = os.path.splitext(os.path.basename(zip_file))[0]
        extracted_folder = os.path.join(folder_path, base_name)

        if os.path.isdir(extracted_folder): #checks if there's a folder with the same name as the zip file
            try:
                send2trash(zip_file)
                deleted.append(zip_file)
            except Exception:
                pass

    if deleted:
        message = f"sent {len(deleted)} .zip file(s) to Recycle Bin :)"
    else:
        message = "no extracted .zip files found to delete,all good!"

    ctypes.windll.user32.MessageBoxW(0, message, "ZIP Cleaner", 1)

if __name__ == "__main__":
    downloads_folder = str(Path.home() / "Downloads")
    delete_extracted_zips(downloads_folder)
