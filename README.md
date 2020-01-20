# batteryBug
Progam tracking Laptop Battery Events using the Battery Management System API on Windows 7

## Configuration
Set the following variables of **BatteryBug.py**:
- `SSID='IoTRaspberryPi3'`: SSID of the room
- `DOMAIN = 'estia.local'`: DNS of the building
- `URL = 'http://itame.pythonanywhere.com/CairnFORM/post/'`: URL for post requests
- `DELAY = 60`:  delay between requests
- `DEBUG = False`: debug mode flag

## Compilation
- `pip install pyinstaller`
- `pyinstaller BatteryBug.spec`

## Installation
- Copy and Paste **dist/BatteryBug.exe** into **C:/Program Files (x86)/BatteryBug/**
- Create a Shortcut of **C:\Program Files (x86)\BatteryBug\BatteryBug.exe** and add it to startup programs