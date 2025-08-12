import os
import shutil

# =============================
# Task: Move all .jpg files to a new folder
# =============================

# Source folder containing files (change this path to your actual folder)
source_folder = r"C:\Users\USER\OneDrive\Desktop\Code_Alpha\CodeAlpha_TaskAutomationwithPythonScripts\source_images"

# Destination folder for .jpg files
destination_folder = r"C:\Users\USER\OneDrive\Desktop\Code_Alpha\CodeAlpha_TaskAutomationwithPythonScripts\jpg_images"

# Check if source folder exists
if not os.path.exists(source_folder):
    print(f"❌ Error: Source folder '{source_folder}' does not exist.")
    exit()

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through files in the source folder
files_moved = 0
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, dest_path)
        files_moved += 1

print(f"✅ {files_moved} .jpg file(s) moved from '{source_folder}' to '{destination_folder}'.")
