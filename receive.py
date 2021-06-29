#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import re
import time
import datetime
import handle
import writefile


file_path_source = input("Please input the file path\n")
file_log = open(file_path_source, 'r')
if not os.path.exists('./data'):
    os.makedirs('./data')
# data_path = os.path.abspath('./data/data.js')
# data_path = './data/data.js'
file_data = open('./data/data.js', "w")

OLED = []
AUDIO = []
MICROPHONE = []
MOTOR = []
PPG = []
COMPASS = []
BAROMATER = []
A_G = []
BT_BLE = []
STM32 = []
LIGHT_SENSOR = []
GPS = []
WIFI = []
NFC = []
EMMC = []
RAM = []
KEY = []
BATTERY = []
TEMPERATURE = []
BATTERY_LINE = []
BATTERY_LEVEL = []

index = 0
while 1:
    line = file_log.readline()
    if not line:
        break
    elif line.isspace():
        # This line is empty
        pass
    else:
        matchObj = re.split(r' ', line)
        if 99 == int(matchObj[1]):
            lc_tick_0 = matchObj[0]
            lc_group_id = matchObj[1]
            timestring = matchObj[2] + ' ' + matchObj[3]
            lc_timestamp_0 = time.mktime(datetime.datetime.strptime(timestring, "%Y-%m-%d %H:%M:%S").timetuple())
        elif 1 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            AUDIO.append(str)
        elif 2 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            MICROPHONE.append(str)
        elif 3 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            MOTOR.append(str)
        elif 4 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            PPG.append(str)
        elif 5 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            COMPASS.append(str)
        elif 6 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            BAROMATER.append(str)
        elif 7 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            A_G.append(str)
        elif 8 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            BT_BLE.append(str)
        elif 9 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            STM32.append(str)
        elif 12 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            LIGHT_SENSOR.append(str)
        elif 13 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            GPS.append(str)
        elif 14 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            OLED.append(str)
        elif 15 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            WIFI.append(str)

        elif 16 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            NFC.append(str)
        elif 17 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            EMMC.append(str)
        elif 18 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            RAM.append(str)
        elif 19 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            KEY.append(str)
        elif 20 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            lc_type = matchObj[2]
            if int(lc_type) == 0:
                BATTERY_LEVEL.append(str)
                str = handle.formatElementLevel(lc_tick_0, lc_timestamp_0, matchObj)
                BATTERY_LINE.append(str)
            else:
                BATTERY.append(str)
        elif 21 == int(matchObj[1]):
            str = handle.formatElement(lc_tick_0, lc_timestamp_0, matchObj)
            TEMPERATURE.append(str)
        else:
            continue
        index = index + 1

AUDIO = handle.formatList(AUDIO)
MICROPHONE = handle.formatList(MICROPHONE)
MOTOR = handle.formatList(MOTOR)
PPG = handle.formatList(PPG)
COMPASS = handle.formatList(COMPASS)
BAROMATER = handle.formatList(BAROMATER)
A_G = handle.formatList(A_G)
BT_BLE = handle.formatList(BT_BLE)
STM32 = handle.formatList(STM32)
LIGHT_SENSOR = handle.formatList(LIGHT_SENSOR)
GPS = handle.formatList(GPS)
OLED = handle.formatList(OLED)
WIFI = handle.formatList(WIFI)
NFC = handle.formatList(NFC)
EMMC = handle.formatList(EMMC)
RAM = handle.formatList(RAM)
KEY = handle.formatList(KEY)
BATTERY_LEVEL = handle.formatList(BATTERY_LEVEL)
BATTERY = handle.formatList(BATTERY)
TEMPERATURE = handle.formatList(TEMPERATURE)

writefile.write_battery_data_to_file(file_data, BATTERY_LINE)

file_data.write("var power_log_data=[\n")

writefile.write_moudel_data_to_file(file_data, OLED)
writefile.write_moudel_data_to_file(file_data, AUDIO)
writefile.write_moudel_data_to_file(file_data, MICROPHONE)
writefile.write_moudel_data_to_file(file_data, MOTOR)
writefile.write_moudel_data_to_file(file_data, PPG)
writefile.write_moudel_data_to_file(file_data, COMPASS)
writefile.write_moudel_data_to_file(file_data, BAROMATER)
writefile.write_moudel_data_to_file(file_data, A_G)
writefile.write_moudel_data_to_file(file_data, BT_BLE)
writefile.write_moudel_data_to_file(file_data, STM32)
writefile.write_moudel_data_to_file(file_data, LIGHT_SENSOR)
writefile.write_moudel_data_to_file(file_data, GPS)
writefile.write_moudel_data_to_file(file_data, WIFI)
writefile.write_moudel_data_to_file(file_data, NFC)
writefile.write_moudel_data_to_file(file_data, EMMC)
writefile.write_moudel_data_to_file(file_data, RAM)
writefile.write_moudel_data_to_file(file_data, KEY)
writefile.write_moudel_data_to_file(file_data, BATTERY)
writefile.write_moudel_data_to_file(file_data, TEMPERATURE)
writefile.write_moudel_data_to_file(file_data, BATTERY_LEVEL)

file_data.write("];")
file_data.close()
file_log.close()

print("Program is running,please wait a few seconds...")
time.sleep(2)

os.system(r'.\index.html')
os.system("pause")
