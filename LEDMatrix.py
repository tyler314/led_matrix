class LEDMatrix:
    def __init__(self, microcontroller):
        self.microcontroller = microcontroller
        rows = 16 if self.microcontroller.D is None else 32
        self.matrix = [[0 for _ in range(32)] for _ in range(rows)]

    def __getitem__(self, index):
        return self.matrix[index[0]][index[1]]

    def __setitem__(self, index, value):
        self.matrix[index[0]][index[1]] = value
