from machine import Pin
from time import sleep

LED = Pin(14, Pin.OUT)
PIR = Pin(13, Pin.IN, Pin.PULL_UP)
LED.low()
sleep(3)

while True:
    print(PIR.value())
    if PIR.value() == 1:
        print("Motion Detected! -> LED is now ON")
        LED.high()
        sleep(1)
    else:
        print("No Motion Detected -> LED is OFF")
        LED.low()
        sleep(1)
    