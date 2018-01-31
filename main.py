# main.py -- put your code here!

print('hello this is main.py')

import pyb
import time
import microcontroller
import led_matrix

pyboard = microcontroller.Pyboard()
matrix = led_matrix.LEDMatrix(pyboard)

def set_row():
    # data is written when LAT is low (hypothesis)
    # data is written when CLK goes low to high (hypothesis)
    pyboard.LAT.low()
    pyboard.CLK.low()
    pyboard.B1.high()
    pyboard.G2.high()
    for _ in range(32):
        pyboard.CLK.high()
        pyboard.B1.value(not pyboard.B1.value())
        pyboard.G2.value(not pyboard.G2.value())
        pyboard.R1.value(0)
        pyboard.R2.value(0)
        pyboard.CLK.low()
    pyboard.CLK.high()
    pyboard.LAT.high()

for i in range(8):
    pyboard.OE.value(1)
    matrix._select_row(i)
    pyboard.OE.value(0)
    pyb.delay(400)
    set_row()
    pyb.delay(400)

matrix._turn_off()

