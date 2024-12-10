# whatsapp-backup-script

A Python script to automate WhatsApp backups from your Android device to your computer using ADB (Android Debug Bridge).

## Prerequisites

Before running the script, ensure you have the following:

1. **USB Debugging**: Enable USB debugging on your Android device.
   - To enable USB debugging, go to `Settings > About Phone > Tap "Build Number" 7 times to enable Developer Options`, then go to `Developer Options` and turn on `USB Debugging`.

2. **ADB (Android Debug Bridge)**: 
   - Install the SDK Platform Tools on your computer. You can download it from the official [Android developer website](https://developer.android.com/tools/releases/platform-tools?hl=it).
   - Make sure the path to the `adb.exe` executable is correctly specified in the script or is included in your system’s PATH environment variable.

3. **Python Libraries**: 
   - The script requires `subprocess`, `os`, and other standard Python libraries. You can install any required dependencies using `pip`.

## Usage

1. **Connect your Android device via USB** and ensure USB debugging is enabled.
2. **Insert the correct paths to your devices in the script.**
3. **Run the Python script** on your computer.
   - The script will automatically detect your connected device and begin the backup process, saving WhatsApp data to your specified backup directory on your computer.

## Troubleshooting

- **ADB Path Issues**: 
  If the script raises errors about finding your phone or the ADB executable, ensure USB debugging is enabled on your device. Then, make sure you have the SDK platform tools installed, and verify the path to the `adb.exe` executable is correctly specified in the script.
  
- **Device Detection Errors**: 
  If no devices are detected, double-check that your phone is properly connected and USB debugging is enabled.

