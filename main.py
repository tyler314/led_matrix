import pyb

LEDS = [pyb.LED(i) for i in range(1, 5)]

while True:
    for led in LEDS:
        led.toggle()
        pyb.delay(100)
