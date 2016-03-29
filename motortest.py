import motorsetup

motorsetup.motorforward(50)
time.sleep(10)
print("15")
motorsetup.motorbackward(50)
time.sleep(10)
print("30")
motorsetup.motorforward(100)
time.sleep(10)
print("45")
motorsetup.motorbackward(100)
time.sleep(10)
print("Done")

print ("The motor should have moved. If not, check power supply")
