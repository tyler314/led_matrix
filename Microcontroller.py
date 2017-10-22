from Singleton import Singleton
import pyb.Pin.board as pins
import pyb

class Microcontroller(metaclass = Singleton):

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
        self.set_RGB_pins()
        self.set_row_select_pins()

    def set_RGB_pins(self, R1, R2, B1, B2, G1, G2):
        raise NotImplementedError('Need to implement set_RGB_data method.')

    def set_row_select_pins(A, B, C, D):
        raise NotImplementedError('Need to implement set_row_select method.')


class Pyboard(Microcontroller):

    def set_RGB_pins(self, R1=pins.Y1, R2=pins.Y2, B1=pins.Y3, B2=pins.Y4, G1=pins.Y5, G2=pins.Y6):
        self.R1 = R1
        self.R2 = R2
        self.B1 = B1
        self.B2 = B2
        self.G1 = G1
        self.G2 = G2

    def set_row_select_pins(self, A=pins.Y7, B=pins.Y8, C=pins.X9, D=pins.X10)
        self.A = A
        self.B = B
        self.C = C
        self.D = D
