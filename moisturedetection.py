import spidev
import time
import os
import motorsetup

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
   adc = spi.xfer2([1,(8+channel)<<4,0])
   data = ((adc[1]&3) << 8) + adc[2]
   return data


# Main loop - read raw data and display
while True:
   soilOne = ReadChannel(2)
   
while soilOne > 500:
  forward(50)
  
while soilOne < 500:
  backward(50)
