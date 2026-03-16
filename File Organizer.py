import os
from tkinter import filedialog
def organize_files():
    folder_path = filedialog.askdirectory(title="Select Folder to Organize")
    if not folder_path:
        print("No folder selected. Exiting.")
        return 
    for foldername, subfolder, filenames in os.walk(folder_path):
        for file in filenames:
            name,ext = os.path.splitext(file)
            ext = ext[1:].upper()
            if ext:
                ext_folder = os.path.join(folder_path, ext)
                if not os.path.exists(ext_folder):
                    os.makedirs(ext_folder)
                if not os.path.exists(dst):
                    os.rename(src, dst)
                src = os.path.join(foldername, file)
                dst = os.path.join(ext_folder, file)
                os.rename(src, dst)
if __name__ == "__main__":
    organize_files()


