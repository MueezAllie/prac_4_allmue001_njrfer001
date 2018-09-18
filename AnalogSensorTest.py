import spidev
from time import sleep
import os
import RPi.GPIO as GPIO
import Adafruit_MCP3008

#Pin Definition
GPIO.setmode(GPIO.BOARD)

SPICLK = 23
SPIMISO = 21
SPIMOSI = 19
SPICE0 = 24

GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICE0, GPIO.OUT)

#First Open up SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

#Initialise what sensor is where
LightChannel = 0
TempChannel = 1
sleepTime = 1

def getReading(channel):
    # First pull the raw data from the chip
    rawData = spi.xfer([1, (8 + channel) << 4, 0])
    #Process the raw data into something we understand
    processedData = ((rawData[1]&3) << 8) + rawData[2]
    return processedData

while True:
    data = getReading(LightChannel)
    print(data)
    data = getReading(TempChannel)
    print(data)
    sleep(sleepTime)
    
GPIO.cleanup()
