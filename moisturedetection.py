import mcp3008
import time
import os
import motorsetup

motorsetup.motorpos = motorpos

# Main loop - read raw data and display
while True:
   soilOne = mcp3008.readadc(0)
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
   
