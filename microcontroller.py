from singleton import Singleton
import pyb
import time

pins = pyb.Pin.board

class Microcontroller:

    def __init__(self):
        self.R1 = None
        self.R2 = None
        self.B2 = None
        self.G1 = None
        self.G2 = None
        self.A = None
        self.B = None
        self.C = None
        self.D = None
        self.OE = None
        self.LAT = None
        self.set_RGB_pins()
        self.set_row_select_pins()
        self.set_control_pins()

    def set_RGB_pins(self, R1, R2, B1, B2, G1, G2):
        raise NotImplementedError('Need to implement set_RGB_data method.')

    def set_row_select_pins(A, B, C, D):
        raise NotImplementedError('Need to implement set_row_select method.')
        
    def latch(self):
        self.LAT.value(0)
        pyb.udelay(500)
        self.LAT.value(1)
            


class Pyboard(Microcontroller):

    def set_RGB_pins(self, R1=pins.Y1, R2=pins.Y2, B1=pins.Y3, B2=pins.Y4, G1=pins.Y5, G2=pins.Y6):
        self.R1 = pyb.Pin(R1, pyb.Pin.OUT) 
        self.R2 = pyb.Pin(R2, pyb.Pin.OUT)
        self.B1 = pyb.Pin(B1, pyb.Pin.OUT)
        self.B2 = pyb.Pin(B2, pyb.Pin.OUT)
        self.G1 = pyb.Pin(G1, pyb.Pin.OUT)
        self.G2 = pyb.Pin(G2, pyb.Pin.OUT)

    def set_row_select_pins(self, A=pins.Y7, B=pins.Y8, C=pins.X9, D=pins.X10):
        self.A = pyb.Pin(A, pyb.Pin.OUT)
        self.B = pyb.Pin(B, pyb.Pin.OUT)
        self.C = pyb.Pin(C, pyb.Pin.OUT)
        self.D = pyb.Pin(D, pyb.Pin.OUT)
        
    def set_control_pins(self, LAT=pins.X11, OE=pins.X12):
        self.LAT = pyb.Pin(LAT, pyb.Pin.OUT)
        self.LAT.value(1)
        self.OE = pyb.Pin(OE, pyb.Pin.OUT)