def T(x):
    if not hasattr(x, '__iter__'):
        # Not a list
        return x
    elif len(x) and not hasattr(x[0], '__iter__'):
        # List of items
        return list(map(list, zip(x)))
    else:
        # List of lists
        return list(map(list, zip(*x)))

class LEDMatrix(list):

    def __init__(self, microcontroller):
        self.microcontroller = microcontroller
        rows = 16 if self.microcontroller.D is None else 32
        super().__init__([[0 for _ in range(32)] for _ in range(rows)])

    def __setitem__(self, index, value):
        return self.setitem(self, index, value)
    
    def __getitem__(self, index):
        if type(index) is tuple:
            return self.getitem(self, index)
        else:
            return super().__getitem__(index)

    def getitem(self, matrix, index):
        if len(index) == 1:
            out = matrix.__getitem__(index[0])
            return out[0] if len(out) == 1 else out
        else:
            return self.getitem(T(matrix.__getitem__(index[0])), index[1:])
            
    def setitem(self, matrix, index, value):
        if type(index) is int or len(index) == 1:
            # recursively evaluate the indices
            index = index[0] if type(index) is not int else index
            matrix_element = matrix.__getitem__(index)
            if hasattr(matrix_element, '__iter__'):
                # recursively evaluate all nested lists within matrix
    	        for i, element in enumerate(matrix_element):
                    if hasattr(element, '__iter__'):
                        for j, _ in enumerate(element):
                            self.setitem(element, j, value)
                    else:
                        matrix_element.__setitem__(i, value)
            else:
                return matrix.__setitem__(index, value)
        else:
            return self.setitem(matrix.__getitem__(index[0]), index[1:], value)