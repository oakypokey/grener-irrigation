import RPi.GPIO as GPIO
import time

# Variables
motorpos = 0
delay = 0.0055
steps = 500
x = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Enable GPIO pins for  ENA and ENB for stepper

enable_a = 38
enable_b = 40

# Enable pins for IN1-4 to control step sequence

coil_A_1_pin = 37
coil_A_2_pin = 35
coil_B_1_pin = 33
coil_B_2_pin = 31

# Set pin states

GPIO.setup(enable_a, GPIO.OUT)
GPIO.setup(enable_b, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Set ENA and ENB to high to enable stepper

GPIO.output(enable_a, True)
GPIO.output(enable_b, True)

# Function for step sequence

def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

# loop through step sequence based on number of steps

def motorforward(i):
  a = 0
  global motorpos
  motorpos = motorpos + i
  return motorpos
  while (a < i):
    setStep(1,0,1,0)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(1,0,0,1)
    time.sleep(delay)
    a = a + 1

# Reverse previous step sequence to reverse motor direction

def motorbackward(i):
  a = 0
  global motorpos
  motorpos = motorpos - i
  return motorpos
  while (a < i):
    setStep(1,0,0,1)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(1,0,1,0)
    time.sleep(delay)
    a = a + 1


