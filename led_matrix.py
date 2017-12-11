class LEDMatrix(object):
    
    def __init__(self, microcontroller):
        self.mc = microcontroller

    def _select_row(self, row):
        row = row % 8 if self.mc.smallBoard else row % 16
        if row & 0x1:
            self.mc.A.value(1)
        else:
            self.mc.A.value(0)
        if row & 0x1 << 1:
            self.mc.B.value(1)
        else:
            self.mc.B.value(0)
        if row & 0x1 << 2:
            self.mc.C.value(1)
        else:
            self.mc.C.value(0)
        if row & 0x1 << 3:
            self.mc.D.value(1)
        else:
            self.mc.D.value(0)

    def _turn_on(self):
        self.mc.OE.value(0)

    def _turn_off(self):
        self.mc.OE.value(1)

    def _toggle_on_off(self):
        value = 0 if self.mc.OE.value() else 1
        self.mc.OE.value(value)

    def set_pixel(i, j, color):
        raise NotImplementedError
