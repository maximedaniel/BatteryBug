# batteryBug
Progam tracking BMS events.

## Configuration
Set the following variables of 'BatteryBug.py':
- SSID='IoTRaspberryPi3' # The SSID of the room <-> proximity level 2
- DOMAIN = 'estia.local' # The DNS of the building <-> proximity level 1
- URL = 'http://itame.pythonanywhere.com/CairnFORM/post/' # url to request for posting information
- DELAY = 60 # request every 1 minute
- DEBUG = False # set DEBUG to false for building

## Compilation
- pip install pyinstaller
- pyinstaller BatteryBug.spec

## Installation
- Copy and Paste 'dist/BatteryBug.exe' into 'C:\Program Files (x86)\BatteryBug\'
- Create a Shortcut of 'C:\Program Files (x86)\BatteryBug\BatteryBug.exe' and add it to startup programs