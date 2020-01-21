import wmi
import os
import shelve
from datetime import datetime
from enum import Enum
from uuid import getnode as get_mac
import csv
import time
import requests
import json
import psutil 
from collections import OrderedDict
from subprocess import check_output
from xml.etree.ElementTree import fromstring
from ipaddress import IPv4Interface, IPv6Interface
import getpass
import ctypes  # An included library with Python install.
import subprocess
import os, os.path
import sys


SSID='IoTRaspberryPi3' # The SSID of the room <-> proximity level 2
DOMAIN = 'estia.local' # The DNS of the building <-> proximity level 1
URL = 'http://itame.pythonanywhere.com/CairnFORM/post/' # url to request for posting information
DELAY = 60 * 5 # request every 5 minutes
DEBUG = False # set DEBUG to false for building

def subprocess_args(include_stdout=True):
    if hasattr(subprocess, 'STARTUPINFO'):
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        env = os.environ
    else:
        si = None
        env = None
    if include_stdout:
        ret = {'stdout': subprocess.PIPE}
    else:
        ret = {}
    ret.update({'stdin': subprocess.PIPE,
                'stderr': subprocess.PIPE,
                'startupinfo': si,
                'env': env })
    return ret


def locateUser():
	try:
		results = str(subprocess.check_output(["netsh", "wlan", "show", "all"],  **subprocess_args(False)))
		results = str(results)
		sentences = results.split(r"\r\n")
		for sentence in sentences:
			if sentence.startswith(r'SSID') and sentence.endswith(SSID): 
				return 2
		nics = getnifs()
		for nic in nics:
			if nic['domain'] == DOMAIN:
				return 1
		return 0
	except OSError as e:
		return 0


def popup(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def getnifs() :

    cmd = 'wmic.exe nicconfig where "IPEnabled  = True" get ipaddress,MACAddress,IPSubnet,DNSHostName, DNSDomain,Caption,DefaultIPGateway /format:rawxml'
    xml_text = check_output(cmd, **subprocess_args(False))
    xml_root = fromstring(xml_text)
    nics = []
    keyslookup = {
        'DNSHostName' : 'hostname',
        'DNSDomain' : 'domain',
        'IPAddress' : 'ip',
        'IPSubnet' : '_mask',
        'Caption' : 'hardware',
        'MACAddress' : 'mac',
        'DefaultIPGateway' : 'gateway',
    }

    for nic in xml_root.findall("./RESULTS/CIM/INSTANCE") :
        # parse and store nic info
        n = {
            'hostname':'',
            'domain':'',
            'ip':[],
            '_mask':[],
            'hardware':'',
            'mac':'',
            'gateway':[],
        }
        for prop in nic :
            name = keyslookup[prop.attrib['NAME']]
            if prop.tag == 'PROPERTY':
                if len(prop):
                    for v in prop:
                        n[name] = v.text
            elif prop.tag == 'PROPERTY.ARRAY':
                for v in prop.findall("./VALUE.ARRAY/VALUE") :
                    n[name].append(v.text)
        nics.append(n)
        # creates python ipaddress objects from ips and masks
        for i in range(len(n['ip'])) :
            arg = '%s/%s'%(n['ip'][i],n['_mask'][i])
            if ':' in n['ip'][i] : n['ip'][i] = IPv6Interface(arg)
            else : n['ip'][i] = IPv4Interface(arg)
        del n['_mask']
    return nics

def isPlugged(battery) :
	return battery.BatteryStatus == 2 or (battery.BatteryStatus > 6 and battery.BatteryStatus < 9)

def post(ans) :
	print('posting data...') if DEBUG else 0
	r = requests.post(URL, json=ans)
	return r.status_code

def init():
	print('loading the json file...') if DEBUG else 0
	with open(logFileName, "a+") as jsonFile:
		try :
			data = json.load(jsonFile)
		except:
			data = {
			'Timestamp': [],
			'Username': [],
			'Plugged': [],
			'Near': [],
			'Availability': [],
			'BatteryRechargeTime': [],
			'BatteryStatus': [],
			'Caption': [],
			'Chemistry':[],
			'ConfigManagerErrorCode':[],
			'ConfigManagerUserConfig':[],
			'CreationClassName':[],
			'Description':[],
			'DesignCapacity':[],
			'DesignVoltage':[],
			'DeviceID':[],
			'ErrorCleared':[],
			'ErrorDescription':[],
			'EstimatedChargeRemaining':[],
			'EstimatedRunTime':[],
			'ExpectedBatteryLife':[],
			'ExpectedLife':[],
			'FullChargeCapacity':[],
			'LastErrorCode':[],
			'MaxRechargeTime':[],
			'Name':[],
			'PNPDeviceID':[],
			'PowerManagementSupported':[],
			'SmartBatteryVersion':[],
			'Status':[],
			'StatusInfo':[],
			'SystemCreationClassName':[],
			'SystemName':[],
			'TimeOnBattery':[],
			'TimeToFullCharge':[]
			}
		jsonFile.close()
	return data


def store(ans):
	print("storing in json file...") if DEBUG else 0
	with open(logFileName, "w+") as jsonFile:
		for key in ans.keys():
			data[key].append(ans[key])
		jsonFile.seek(0)  # rewind
		jsonFile.write(json.dumps(data))
		jsonFile.truncate()
		jsonFile.close()

def clear():
	print("clearing the json file...") if DEBUG else 0
	with open(logFileName, "w+") as jsonFile:
	    jsonFile.seek(0)  # rewind
	    jsonFile.write(json.dumps(data))
	    jsonFile.truncate()
	    jsonFile.close()
	return {
				'Timestamp': [],
				'Username': [],
				'Plugged': [],
                'Near': [],
                'Availability': [],
                'BatteryRechargeTime': [],
                'BatteryStatus': [],
                'Caption': [],
                'Chemistry':[],
                'ConfigManagerErrorCode':[],
                'ConfigManagerUserConfig':[],
                'CreationClassName':[],
                'Description':[],
                'DesignCapacity':[],
                'DesignVoltage':[],
                'DeviceID':[],
                'ErrorCleared':[],
                'ErrorDescription':[],
                'EstimatedChargeRemaining':[],
                'EstimatedRunTime':[],
                'ExpectedBatteryLife':[],
                'ExpectedLife':[],
                'FullChargeCapacity':[],
                'LastErrorCode':[],
                'MaxRechargeTime':[],
                'Name':[],
                'PNPDeviceID':[],
                'PowerManagementSupported':[],
                'SmartBatteryVersion':[],
                'Status':[],
                'StatusInfo':[],
                'SystemCreationClassName':[],
                'SystemName':[],
                'TimeOnBattery':[],
                'TimeToFullCharge':[]
			}

def postLog():
	print("parsing the json file...") if DEBUG else 0
	for i in range(len(data['Username'])):
		ans = {}
		for key in data.keys():
			ans[key] = data[key][i]
		try :
			status = post(ans)
			if status !=200 :
				print('POST not ok.') if DEBUG else 0
			else :
				print('POST ok.') if DEBUG else 0
		except :
			print('POST failed.') if DEBUG else 0
			store(ans)

	return clear()

def getUser():
	username = getpass.getuser()
	nics = getnifs()
	res = 'none'
	for nic in nics :
		if nic['domain'] == DOMAIN:
			res = DOMAIN
	return username, res

#### MAIN ###
c = wmi.WMI ()
logFileName = os.getenv('APPDATA')+'\BatteryBug.json'
data = init()
UNKNOW = -1
NO = 0
YES = 1
plugged = UNKNOW
battery_level = UNKNOW
recharge_level = UNKNOW
shifting = NO
battery = None
if len(c.Win32_Battery ()):
	battery = c.Win32_Battery ()[0]

while True :
	if battery is not None and battery.EstimatedChargeRemaining is not None and battery.BatteryStatus is not None:
		ans = {}
		bannedProps = ['InstallDate', 'PowerManagementCapabilities']
		for prop in battery.__dict__['_properties']:    # TypeError: 'list' object is not callable
			if prop not in bannedProps:
				ans[prop] =  getattr(battery, prop) 
		ans['Timestamp'] =  datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') 
		ans['Username'] =   getpass.getuser()
		ans['Plugged'] =   isPlugged(battery)
		ans['Near'] =   locateUser()
		try :
			status = post(ans)
			if status !=200 :
				print('POST not ok. Storing data for next posting...') if DEBUG else 0
				store(ans)
			else :
				print('POST ok. Posting previous data...') if DEBUG else 0
				data = postLog()
		except :
			print('POST failed.') if DEBUG else 0
			store(ans)

	time.sleep(DELAY)
	battery = None
	if len(c.Win32_Battery ()):
		battery = c.Win32_Battery ()[0]
