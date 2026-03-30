humidity_file = open('/Users/zoefulton/Downloads/Smartpix_files/Smartpix_code/test_20260326.txt', 'r', encoding='latin-1')  # need to change this to path on lab computer
humidity_data = humidity_file.read()

def last_humidity_value(file):
    # find last line of humidity data
    humidity_lines = file.splitlines()
    last_line = humidity_lines[len(humidity_lines)-1]

    # split last line into list of characters
    last_line_split = list(last_line)
    last_5_characters = last_line_split[-5:]

    # join last 5 characters into string and convert it into a integer
    last_5_characters = ''.join(last_5_characters)
    last_5_characters = float(last_5_characters)
    return last_5_characters

humidity = last_humidity_value(humidity_data)

#functions to turn on and off switch 1 based on humidity value
import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

def on_switch_1():
    ser = serial.Serial("/dev/cu.usbserial-11210", 9600, timeout=1) # will need to change device name on lab computer
    data = bytearray([0xA0, 0x01, 0x01, 0xA2])
    ser.write(data)
    return "Switch 1 ON"

def off_switch_1():
    ser = serial.Serial("/dev/cu.usbserial-11210", 9600, timeout=1)
    data = bytearray([0xA0, 0x01, 0x00, 0xA1])
    ser.write(data)
    return "Switch 1 OFF"

if humidity >= 50:
    off_switch_1()
    print("Humidity has reached threshold level, turning off electronics.")