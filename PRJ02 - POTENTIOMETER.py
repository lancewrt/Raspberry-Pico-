from machine import Pin, ADC	#import Pin and ADC class
from time import sleep #import sleep class

potentiometer = ADC(28)		#create an object named potentiometer using ADC class

while True:
    potentiometer_value = potentiometer.read_u16()	#read analog pin
    print(potentiometer_value)		#print ADC value
    
    sleep(0.25)		#sleep interval