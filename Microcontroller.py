from Singleton import Singleton

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

    def set_RGB_data(self, R1, R2, B1, B2, G1, G2):
        raise NotImplementedError('Need to implement set_RGB_data method.')

    def set_row_select(A, B, C, D):
        raise NotImplementedError('Need to implement set_row_select method.')
