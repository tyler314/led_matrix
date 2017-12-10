class LEDMatrix(object):
    
    def __init__(self, microcontroller):
        self.mc = microcontroller

    def set_pixel(i, j, color):
        raise NotImplementedError
