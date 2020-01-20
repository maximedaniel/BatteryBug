# batteryBug
Progam tracking BMS events.

## Configuration
Set the following variables of **BatteryBug.py**:
- `SSID='IoTRaspberryPi3'`: SSID of the room (proximity level 2)
- `DOMAIN = 'estia.local'`: DNS of the building (proximity level 1)
- `URL = 'http://itame.pythonanywhere.com/CairnFORM/post/'`: URL for posting information
- `DELAY = 60`:  request every 1 minute
- `DEBUG = False`: debugging mode

## Compilation
- pip install pyinstaller
- pyinstaller BatteryBug.spec

## Installation
- Copy and Paste **dist/BatteryBug.exe** into **C:\Program Files (x86)\BatteryBug\**
- Create a Shortcut of **C:\Program Files (x86)\BatteryBug\BatteryBug.exe** and add it to startup programs