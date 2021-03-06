#1/usr/bin/env python
#Program to read an analogue input on Custard Pi 3
#www.sf-innovations.co.uk

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(24, GPIO.OUT)    #pin 24 is chip enable
GPIO.setup(23, GPIO.OUT)    #pin 23 is clock  
GPIO.setup(19, GPIO.OUT)    #pin 19 is data out
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)     #pin 21 is data in

#set pins to default state
GPIO.output(24, True)       
GPIO.output(23, False)
GPIO.output(19, True)

#set address channels 0 to 7
#1st bit selects single/differential
#2nd bit channel address
#3rd bit channel address
#4th bit channel address
#5th bit 1 bit delay for data
#6th bit 1st null bit of data

def readanalog(y):
    GPIO.output(19, True)
    #select the right channel
    if y == 0:
        word= [1 ,1, 0, 0, 0, 1, 1]     #set channel 0                                                                                                                                                                
    if y == 1:
        word= [1 ,1, 0, 0, 1, 1, 1]     #set channel 1
    if y == 2:
        word= [1 ,1, 0, 1, 0, 1, 1]     #set channel 2
    if y == 3:
        word= [1 ,1, 0, 1, 1, 1, 1]     #set channel 3
    if y == 4:
        word= [1 ,1, 1, 0, 0, 1, 1]     #set channel 4
    if y == 5:
        word= [1 ,1, 1, 0, 1, 1, 1]     #set channel 5
    if y == 6:
        word= [1 ,1, 1, 1, 0, 1, 1]     #set channel 6
    if y == 7:
        word= [1 ,1, 1, 1, 1, 1, 1]     #set channel 7
    if y == 8:
        word= [1 ,0, 0, 0, 0, 1, 1]     #set diff ch0 +ve ch1 -ve
    if y == 9:
        word= [1 ,0, 0, 0, 1, 1, 1]     #set diff ch0 -ve ch1 +ve
    if y == 10:
        word= [1 ,0, 0, 1, 0, 1, 1]     #set diff ch2 +ve ch3 -ve
    if y == 11:
        word= [1 ,0, 0, 1, 1, 1, 1]     #set diff ch2 -ve ch3 +ve
    if y == 12:
        word= [1 ,0, 1, 0, 0, 1, 1]     #set diff ch4 +ve ch5 -ve
    if y == 13:
        word= [1 ,0, 1, 0, 1, 1, 1]     #set diff ch4 -ve ch5 +ve
    if y == 14:
        word= [1 ,0, 1, 1, 0, 1, 1]     #set diff ch6 +ve ch7 -ve
    if y == 15:
        word= [1 ,0, 1, 1, 1, 1, 1]     #set diff ch6 -ve ch7 +ve

    GPIO.output(24, False)  #enable chip
    anip=0  #clear variable

    #clock out 7 bits to select channel
    for x in range (0,7):
        GPIO.output(19, word[x])
        time.sleep(0.01)
        GPIO.output(23, True)
        time.sleep(0.01)
        GPIO.output(23, False)

     #clock in 11 bits of data
    for x in range (0,12):
        GPIO.output(23,True)    #set clock hi
        time.sleep(0.01)
        bit=GPIO.input(21)      #read input
        time.sleep(0.01)
        GPIO.output(23,False)   #set clock lo
        value=bit*2**(12-x-1)   #work out value of this bit
        anip=anip+value         #add to previous total
        #print (bit,value,anip)    
    GPIO.output(24, True)       #disable chip

    volt = anip*2.5/4096        #use ref voltage of 2.5 to work out voltage
    #volt = ("%.2f" %round(volt,2))  #round to 2 decimal places
    #print "voltage ch", y, volt #print to screen
    return volt
