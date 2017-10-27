# --- functions ----------------------------------------------------------------------------------


def transpose(x):
    if not hasattr(x, '__iter__'):
        # not a list
        return x
    elif len(x) and not hasattr(x[0], '__iter__'):
        # list of items
        return list(map(list, zip(x)))
    else:
        # list of lists
        return list(map(list, zip(*x)))


# --- classes ------------------------------------------------------------------------------------


class NDList(list):

    def __init__(self, shape, fill=0.):
        lis = fill
        for s in shape[::-1]:
            lis = [lis] * s
        list.__init__(self, lis)

    def __setitem__(self, index, value):
        return self.setitem(self, index, value)
    
    def __getitem__(self, index):
        if type(index) is tuple:
            return self.getitem(self, index)
        else:
            return super().__getitem__(index)

    @property
    def shape(self):
        shape = []
        item = self
        while hasattr(item, '__len__'):
            shape.append(len(item))
            item = item[0]
        return tuple(shape)

    @property
    def size(self):
        out = 1
        for s in self.shape:
            out *= s
        return out

    def getitem(self, matrix, index):
        if len(index) == 1:
            out = matrix.__getitem__(index[0])
            return out[0] if len(out) == 1 else out
        else:
            return self.getitem(transpose(matrix.__getitem__(index[0])), index[1:])
            
    def setitem(self, matrix, index, value):
        if type(index) in [int, slice] or len(index) == 1:
            # recursively evaluate the indices
            index = index[0] if type(index) not in [int, slice] else index
            if type(index) is int:
                self._scan_matrix(matrix, index, value, matrix.__getitem__(index))
            elif type(index) is slice:
                start = index.start if index.start is not None else 0
                stop = index.stop if index.stop is not None else len(matrix)
                step = index.step if index.step is not None else 1
                for i in range(start, stop, step):
                    self._scan_matrix(matrix, i, value)
        else:
            return self.setitem(matrix.__getitem__(index[0]), index[1:], value)

    def _scan_matrix(self, matrix, index, value):
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
