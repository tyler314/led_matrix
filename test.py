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
        

class test(list):

    def __setitem__(self, index, value):
        if type(index) is tuple:
            return self.setitem(self, index, value)
        else:
            return super().__setitem__(index, value)
    
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
    	if len(index) == 1:
    		return matrix.__setitem__(index[0], value)
    	else:
    		return self.setitem(matrix.__getitem__(index[0]), index[1:], value)
