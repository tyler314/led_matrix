from Microcontroller import Microcontroller
import pyb.Pin.board as pins
import pyb

class Pyboard(Microcontroller):

    def set_RGB_data(self, R1=pins.Y1, R2=pins.Y2, B1==pins.Y3, B2=pins.Y4, G1=pins.Y5, G2=pins.Y6):
        self.R1 = R1
        self.R2 = R2
        self.B1 = B1
        self.B2 = B2
        self.G1 = G1
        self.G2 = G2

    def set_row_select(self, A=pins.Y7, B=pins.Y8, C=pins.X9, D=pins.X10)
        self.A = A
        self.B = B
        self.C = C
        self.D = D
