from machine import Pin, ADC, PWM	#import Pin and ADC class
from time import sleep #import sleep class

led = PWM(Pin(13))
led.freq(1000)
potentiometer = ADC(28)		#create an object named potentiometer using ADC class

while True:
    potentiometer_value = potentiometer.read_u16()	#read analog pin
    print(potentiometer_value)		#print ADC value
    led.duty_u16(potentiometer_value)
    
    sleep(0.25)		#sleep interval
