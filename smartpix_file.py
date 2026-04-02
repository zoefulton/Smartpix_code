import serial
import serial.tools.list_ports
import math
file = "C:/Users/daq/Downloads/test_20260330.txt"
ser = serial.Serial("COM3", 9600, timeout=1) # will need to change device name on lab computer
chip_temperature = -22

def read_humidity_control_switch(file_str, ser, chip_temperature):

    file = open(file_str, 'r', encoding='latin-1')  # need to change this to path on lab computer
    humidity_data = file.read()
#need to go now, but will change everything from file to humidity_data (i think that's the problem) taking switch so can run on own computer
    # get last humidity value from file
    def temperature_humidity_value(file):
        file = file.read()
        humidity_lines = file.splitlines()
        last_line = humidity_lines[len(humidity_lines)-1]
        print("hellow")
        print(last_line)
        humidity_string = last_line.split("\t")[4]
        humidity = float(humidity_string)

        temperature_string = last_line.split("\t")[3] #need to check specific position of temperature
        temperature = float(temperature_string)
        return humidity, temperature,


    # define humidity threshold for turning on/off switch
    def dry_temperature(file):
        humidity, temperature = temperature_humidity_value(file)
        b, c = 17.625, 243.04
        gamma = math.log(humidity/100) + (b*temperature)/(c+temperature)        
        T_dry = (c*gamma)/(b-gamma)
        return T_dry

    #functions to turn on and off switch 1 based on humidity value
    #ports = serial.tools.list_ports.comports()

    def on_switch_1(ser):
        data = bytearray([0xA0, 0x01, 0x01, 0xA2])
        ser.write(data)
        return "Switch 1 ON"

    def off_switch_1(ser):
        data = bytearray([0xA0, 0x01, 0x00, 0xA1])
        ser.write(data)
        return "Switch 1 OFF"

    if dry_temperature(file)+2 <= chip_temperature:
        off_switch_1()
        print("Humidity has reached threshold level, turning off electronics.")
    else:
        print(f"Humidity/temperature is: {temperature_humidity_value(file)} so dewpoint is {dry_temperature(file)}")

print(read_humidity_control_switch(file, ser, chip_temperature))
  