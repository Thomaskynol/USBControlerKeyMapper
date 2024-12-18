# USB Device Key Mapper

A Python script that interacts with a USB device, maps its input values to keyboard arrow keys, and triggers key presses using PyAutoGUI. Designed for use with compatible devices like game controllers or custom USB input devices.

## Features
- Detects and interfaces with a specified USB device.
- Maps device inputs to arrow keys (`Up`, `Down`, `Left`, `Right`).
- Simulates real-time key presses.
- Graceful exit on keyboard interruption.

## Requirements
- Python 3.x
- Libraries:
  - `pyautogui`
  - `usb`

Install required libraries using:
```bash
pip install pyautogui pyusb
