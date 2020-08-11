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
        gpio.output(trig, False)
        time.sleep(0.5)
        gpio.output(trig, True)
        time.sleep(0.00001)
        gpio.output(trig, False)
        while gpio.input(echo) == 0 :
            pulse_start = time.time()

        while gpio.input(echo) == 1 :
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        print("Distance : ", distance, "cm")
        if distance < 10:
            gpio.output(buzzer,gpio.HIGH)
            RED.start(1)
            GREEN.start(100)
            BLUE.start(100)
        else:
            gpio.output(buzzer,gpio.LOW)
            RED.start(100)
            GREEN.start(1)
            BLUE.start(1)

except :
    gpio.cleanup()