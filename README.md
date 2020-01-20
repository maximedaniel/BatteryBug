# batteryBug
Progam tracking Laptop Battery Events using the Battery Management System API on Windows 7

## Configuration
1. Open **BatteryBug.py** 
2. Set the following variables:
    - `SSID='IoTRaspberryPi3'`: SSID of the room
    - `DOMAIN = 'estia.local'`: DNS of the building
    - `URL = 'http://itame.pythonanywhere.com/CairnFORM/post/'`: URL for post requests
    - `DELAY = 60`:  delay between requests
    - `DEBUG = False`: debug mode flag

## Compilation
1. Open a Windows Command Prompt
2. Execute the following commands:
    - `pip install pyinstaller`
    - `pyinstaller BatteryBug.spec`

## Installation
1. Perform the following instructions:
    - Copy and Paste `dist/BatteryBug.exe` into `C:/Program Files (x86)/BatteryBug/`
    - Create a Shortcut of `C:\Program Files (x86)\BatteryBug\BatteryBug.exe` and add it to `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`