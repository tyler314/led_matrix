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
            return matrix.__getitem__(index[0])
        else:
            return self.getitem(matrix.__getitem__(index[0]), index[1:])
            
    def setitem(self, matrix, index, value):
    	if len(index) == 1:
    		return matrix.__setitem__(index[0], value)
    	else:
    		return self.setitem(matrix.__getitem__(index[0]), index[1:], value)