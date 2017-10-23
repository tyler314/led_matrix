class LEDMatrix(list):

    def __init__(self, microcontroller):
        self.microcontroller = microcontroller
        rows = 16 if self.microcontroller.D is None else 32
        super().__init__([[0 for _ in range(32)] for _ in range(rows)])

