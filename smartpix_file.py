import serial
import serial.tools.list_ports
import math
file = "/Users/zoefulton/Downloads/Smartpix_files/Smartpix_code/test_20260326.txt" #my computer
#"C:/Users/daq/Downloads/test_20260330.txt" #lab computer
device = "/dev/cu.usbserial-1320" # my computer
#"COM3" # lab computer
ser = serial.Serial(device, 9600, timeout=1)
chip_temperature = 6

import time
time.sleep(2)

def on_switch_1(ser):
        data = bytearray([0xA0, 0x01, 0x01, 0xA2])
        ser.write(data)
        return "Switch 1 ON"

on_switch_1(ser)

def read_humidity_control_switch(file_str, ser, chip_temperature):

    file_read = open(file_str, 'r', encoding='latin-1')  
    file = file_read.read()

    def temperature_humidity_value(file):
        # finding humidity value from file
        humidity_lines = file.splitlines()
        last_line = humidity_lines[len(humidity_lines)-1]
        humidity_string = last_line.split("\t")[4]
        humidity = float(humidity_string)

        # finding temperature value from file
        temperature_string = last_line.split("\t")[3]
        temperature = float(temperature_string)
        return humidity, temperature,

    # define humidity threshold for turning on/off switch
    def dew_temperature(file): # checked with online calcualtor and was 0.3 degrees off
        humidity, temperature = temperature_humidity_value(file)
        b, c = 17.625, 243.04
        gamma = math.log(humidity/100) + (b*temperature)/(c+temperature)        
        T_dew = (c*gamma)/(b-gamma)
        return T_dew

    def on_switch_1(ser):
        data = bytearray([0xA0, 0x01, 0x01, 0xA2])
        ser.write(data)
        return "Switch 1 ON"

    def off_switch_1(ser):
        data = bytearray([0xA0, 0x01, 0x00, 0xA1])
        ser.write(data)
        return "Switch 1 OFF"

    print 
    if dew_temperature(file)+2 >= chip_temperature:  # i got confused about it should be less than or greater than
        off_switch_1(ser)
        print("Humidity has reached threshold level, turning off electronics.")
    else:
        print(f"Humidity/temperature is: {temperature_humidity_value(file)} so dewpoint is {dew_temperature(file)}")

print(read_humidity_control_switch(file, ser, chip_temperature))
  