import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)


# SETUP
trig = 13
echo = 19
buzzer = 23

green = 27
red = 17
blue = 22
freq = 100

print("Start!")

gpio.setwarnings(False)

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)
gpio.setup(buzzer, gpio.OUT)

gpio.setup(red, gpio.OUT)
gpio.setup(green, gpio.OUT)
gpio.setup(blue, gpio.OUT)

RED = gpio.PWM(red, freq)
GREEN = gpio.PWM(green, freq)
BLUE = gpio.PWM(blue, freq)

try :
    while True :
        # Write Here
        # Hello Dimigo

except :
    gpio.cleanup()