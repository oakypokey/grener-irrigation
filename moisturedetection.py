import mcp3008
import time
import os
import motorsetup

target = 700

# Main loop - read raw data and display
while True:
   soilOne = mcp3008.readadc(0)
   print soilOne
   print motorsetup.motorpos
   if soilOne < target and motorsetup.motorpos == 0:
      motorsetup.motorforward(50)
   elif soilOne < target and motorsetup.motorpos == 50:
      time.sleep(10)
   elif soilOne > target and motorsetup.motorpos == 50:
      motorsetup.motorbackward(5)
   elif soilOne > target and motorsetup.motorpos == 0:
      time.sleep(10)
   elif soilOne == target and motorsetup.motorpos in (0,50):
      time.sleep(10)
   else:
      break
   
print ("System Error. Motor misalignment. Please recalibrate valve and restart")
   
