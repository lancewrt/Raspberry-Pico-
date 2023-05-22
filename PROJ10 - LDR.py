from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)
ldr = Pin(27, Pin.IN, Pin.PULL_DOWN)

while True:
    if ldr.value():
        led.value(0)
        sleep(0.5)
        print(ldr.value())
    else:
        led.value(0)
        sleep(0.5)