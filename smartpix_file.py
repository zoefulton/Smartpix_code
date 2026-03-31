import serial
import serial.tools.list_ports
file = '/Users/zoefulton/Downloads/Smartpix_files/Smartpix_code/test_20260326.txt'
ser = serial.Serial("/dev/cu.usbserial-11210", 9600, timeout=1) # will need to change device name on lab computer

def read_humidity_control_switch(file, humidity):
    humidity_file = open(file, 'r', encoding='latin-1')  # need to change this to path on lab computer
    humidity_data = humidity_file.read()

    # get last humidity value from file
    def last_humidity_value(file):
    # find last line of humidity data
        humidity_lines = file.splitlines()
        last_line = humidity_lines[len(humidity_lines)-1]
        humidity_string = last_line.split("\t")[4]
        humidity = float(humidity_string)
        return humidity
    
    # define humidity threshold for turning on/off switch
    def humidity_threshold(humidity):
        return 50.0

    #functions to turn on and off switch 1 based on humidity value
    #ports = serial.tools.list_ports.comports()

    def on_switch_1():
        data = bytearray([0xA0, 0x01, 0x01, 0xA2])
        ser.write(data)
        return "Switch 1 ON"

    def off_switch_1():
        data = bytearray([0xA0, 0x01, 0x00, 0xA1])
        ser.write(data)
        return "Switch 1 OFF"

    if humidity >= humidity_threshold(humidity):
        off_switch_1()
        print("Humidity has reached threshold level, turning off electronics.")
    
