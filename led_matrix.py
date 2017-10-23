class LEDMatrix(list):

    def __init__(self, microcontroller):
        self.microcontroller = microcontroller
        rows = 16 if self.microcontroller.D is None else 32
        super().__init__([[0 for _ in range(32)] for _ in range(rows)])
        
    def __getitem__(self, index):
        if type(index) is tuple and type(index[0]) is int:
			return super().__getitem__(index[0]).__getitem__(index[1])
		else:
			return super().__getitem__(index)

    def __setitem__(self, index, value):
        if type(index) is int:
            return super().__setitem__(index, value)
        elif type(index) is slice:
            pass
        elif type(index) is tuple:
            if type(index[0]) is int:
                return super().__getitem__(index[0]).__setitem__(index[1], value)
            elif type(index[0]) is slice:
                pass
                
    def setitem_tuple(self, matrix, index, value):
        if len(index) == 1:
            return matrix.__setitem__(index[0], value)
        else:
            return self.setitem_tuple(matrix.__getitem__(tuple[0], tuple(list[1:]), value)