humidity_file = open('C:/Users/daq/Downloads/test_20260330.txt', 'r', encoding='latin-1')  # need to change this to path on lab computer
humidity_data = humidity_file.read()

def last_humidity_value(file):
    # find last line of humidity data
    humidity_lines = file.splitlines()
    last_line = humidity_lines[len(humidity_lines)-1]
    
    humidity = last_line.split('\t')[4]

    humidity_float = float(humidity)
    return humidity_float

humidity = last_humidity_value(humidity_data)
print(humidity)

#functions to turn on and off switch 1 based on humidity value
import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

#ser = serial.Serial("/dev/cu.usbserial-11210", 9600, timeout=1) # will need to change device name on lab computer
ser = serial.Serial("COM3", 9600, timeout=1) # will need to change device name on lab computer
    
def on_switch_1(ser):
    data = bytearray([0xA0, 0x01, 0x01, 0xA2])
    ser.write(data)
    return "Switch 1 ON"

def off_switch_1(ser):
    data = bytearray([0xA0, 0x01, 0x00, 0xA1])
    ser.write(data)
    return "Switch 1 OFF"
import time

on_switch_1(ser)
time.sleep(5)

humidity_threshold = 6
if humidity >= humidity_threshold:
    off_switch_1(ser)
    print("Humidity has reached threshold level, turning off electronics.")