import spidev
import time
import os
import sys

#Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

#Rpi has 1 bus(#0) and 2 device (#0 & #1)

#Function to read ADC data from a channel

def GetData(channel):                       #Channel must be an integer 0-7
    adc = spi.xfer([1,(8+channel)<<4,0])    #Sending 3 bytes
    data = ((adc[1]&3) << 8) + adc[2]

    return data

#Function to convert data to voltage level
#Places: number of decimal places needed

def ConvertVolts(data,places):
    volts = (data*3.3)/float(1023)
    volts = round(volts, places)
    return volts

#Define sensor channels
channel = 0

#Define delay between readings

delay = 0.5

try:
    while True:
        #Read the data
        sensor_data = GetData(channel)
        sensor_volt = ConvertVolts(sensor_data,2)

        print(sensor_data)
        print(sensor_volt)

        #wait before repeating loop
        time.sleep(delay)

except KeyboardInterrupt:
    spi.close()
