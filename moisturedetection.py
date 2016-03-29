import spidev
import time
import os
import motorsetup

motorsetup.motorpos = motorpos
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
   soilOne = readadc(0)
   if soilOne < target and motorpos = 0:
      motorsetup.forward(50)
   elif soilOne < target and motorpos = 50:
      time.sleep(10)
   elif soilOne > target and motorpos = 50:
      motorsetup.backward(5)
   elif soilOne > target and motorpos = 0:
      time.sleep(10)
   elif soilOne = target and motorpos in (0,50):
      time.sleep(10)
   else:
      break
   
print ("System Error. Motor misalignment. Please recalibrate valve and restart")
   
