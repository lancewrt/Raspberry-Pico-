from machine import Pin

led = Pin(14, Pin.OUT)
push_btn = Pin(13, Pin.IN)

while True:
    logic_state = push_btn.value()
    if logic_state == 1:
        led.value(1)
    else:
        led.value(0)