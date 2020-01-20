# BatteryBug

Tracker for Laptop Battery Events using the Battery Management System API on Windows 7

## Configuration

1. Open *BatteryBug.py*
2. Set the following variables:
    - `SSID='IoTRaspberryPi3'`: SSID of the room
    - `DOMAIN = 'estia.local'`: DNS of the building
    - `URL = 'http://itame.pythonanywhere.com/CairnFORM/post/'`: URL for post requests
    - `DELAY = 60`:  delay between requests
    - `DEBUG = False`: debug mode flag

## Compilation

1. Press `Win + R keys`
2. Enter `cmd`
3. Enter `cd <pathToBatteryBugDirectory>`
4. Enter `pip install pyinstaller && pyinstaller BatteryBug.spec`

## Installation

1. Copy and Paste `<pathToBatteryBugDirectory>/dist/BatteryBug.exe` into `C:/Program Files (x86)/BatteryBug/`
2. Create a shortcut for `C:/Program Files (x86)/BatteryBug/BatteryBug.exe` and cut it to `C:/Users/<username>/AppData/Roaming/Microsoft/Windows/Start Menu/Programs\Startup`
