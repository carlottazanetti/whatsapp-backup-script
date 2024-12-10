"""
WhatsApp Backup Script

This script automates the process of backing up WhatsApp files (Backups, 
Databases, and Media)
from an Android phone connected via USB. It uses ADB to access the phone's 
file system 
and copies files to a backup directory.

Features:
- Handles subfolders inside the main folders (Backups, Databases, Media)
- Skips existing files to avoid duplication

Usage:
1. Connect your phone to the PC via USB.
2. Ensure USB debugging is enabled on your phone.
3. Run the script. The script will list devices, and you can select which 
device to use.

Author: Carlotta Zanetti
Date: 10/12/2024
"""

import os
import subprocess


def sync_folder(phone_folder, local_folder):
    """
    Recursively copies files from the phone folder to the local backup folder.
    Preserves subfolder structure and skips files that already exist locally.
    """
    print(f"Syncing folder: {phone_folder} to {local_folder}")
    command = ([adb_path, "-s", device_serial, "shell", "find", 
                phone_folder, "-type", "f"])
    try:
        result = subprocess.run(command, capture_output=True, text=True, 
                                check=True)
        phone_files = result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error accessing {phone_folder} on phone: {e.stderr}")
        return

    for phone_file_path in phone_files:
        relative_path = os.path.relpath(phone_file_path, phone_folder)
        local_file_path = os.path.join(local_folder, relative_path)

        # Create the parent directories for the file if they don't exist
        local_subfolder_path = os.path.dirname(local_file_path)
        os.makedirs(local_subfolder_path, exist_ok=True)

        # Copy the file only if it doesn't already exist locally
        if not os.path.isfile(local_file_path):
            print(f"Copying: {phone_file_path} -> {local_file_path}")
            command = ([adb_path, "-s", device_serial, "pull", 
                        phone_file_path, local_file_path])
            try:
                subprocess.run(command, check=True)
            except subprocess.CalledProcessError as e:
                print("Error copying" +
                    f"{phone_file_path} to {local_file_path}: {e.stderr}")
        else:
            print(f"File already exists, skipping: {local_file_path}")


##### MAIN #####
#  Path to the backup directory
backup_dir = "insert path to the desired backup folder" #TODO insert the correct path
if not os.path.exists(backup_dir):
    raise ValueError("Couldn't find the external disk")

# Full path to ADB executable
adb_path = r"insert path to adb.exe" #TODO insert the correct path
if not os.path.isfile(adb_path):
    raise FileNotFoundError(f"ADB executable not found at path: {adb_path}")

# Get the list of connected devices
result = subprocess.run([adb_path, "devices"], capture_output=True, text=True)
devices = ([line.split()[0] for line in result.stdout.splitlines() 
            if "\tdevice" in line])

# Check for multiple devices
if len(devices) > 1:
    print("Multiple devices detected:")
    for i, device in enumerate(devices, start=1):
        print(f"{i}: {device}")
    selected_device = input("Enter the number of the device you want to use: ")
    device_serial = devices[int(selected_device) - 1]
elif len(devices) == 1:
    device_serial = devices[0]
    print(f"Using connected device: {device_serial}")
else:
    raise ConnectionError("No devices detected. Please connect your phone.")

# Use the selected device in subsequent ADB commands
folders_to_backup = ['Backups', 'Databases', 'Media']
phone_base_path = "path to the Whatsapp folder in your phone" #TODO insert the correct path


for folder_name in folders_to_backup:
    phone_folder_path = os.path.join(phone_base_path, folder_name)
    local_folder_path = os.path.join(backup_dir, folder_name)
    sync_folder(phone_folder_path, local_folder_path)

print("🎉🎉🎉 CONGRATS! 🎉🎉🎉")
print("Backup Completed")
print("Fuck you Google Drive")
