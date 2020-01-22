# BatteryBug

Tracker for laptop battery events using the Battery Management System (BMS) API on Windows 7

## Dependency

1. Install *Python 3.6*
2. Press `Win + R keys`
3. Enter `cmd`
4. Enter `cd <pathToBatteryBugDirectory>`
5. Enter `pip install -r requirements.txt`

## Configuration

1. Open *BatteryBug.py*
2. Set the following variables:
    - `SSID`: SSID of the room
    - `DOMAIN`: DNS of the building
    - `URL`: URL for post requests
    - `DELAY`:  delay between requests
    - `DEBUG`: debug flag

## Compilation

1. Press `Win + R keys`
2. Enter `cmd`
3. Enter `cd <pathToBatteryBugDirectory>`
4. Enter `pip install pyinstaller && pyinstaller BatteryBug.spec`

## Installation

1. Copy and paste `<pathToBatteryBugDirectory>/dist/BatteryBug.exe` into `C:/Program Files (x86)/BatteryBug/`
2. Create a shortcut for `C:/Program Files (x86)/BatteryBug/BatteryBug.exe` and cut it to `C:/Users/<username>/AppData/Roaming/Microsoft/Windows/Start Menu/Programs\Startup`
