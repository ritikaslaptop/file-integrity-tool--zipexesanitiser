import glob
import os
import ctypes
from pathlib import Path
from send2trash import send2trash

def delete_exe_files(folder_path):
    exe_files = glob.glob(os.path.join(folder_path, "*.exe"))
    deleted = []

    for file in exe_files:
        try:
            send2trash(file)  #moves to Recycle Bin
            deleted.append(file)
        except Exception as e:
            pass

    if deleted:
        message = f"sent {len(deleted)} .exe file(s) to Recycle Bin :)"
    else:
        message = "no .exe files found to delete,all good in here!"

    ctypes.windll.user32.MessageBoxW(0, message, "EXE Cleaner", 1)

if __name__ == "__main__":
    downloads_folder = str(Path.home() / "Downloads")
    delete_exe_files(downloads_folder)