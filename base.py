# --- functions ----------------------------------------------------------------------------------


def iteriters(*args):
    # very similar to itertools.product in cpython
    pools = map(tuple, args)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

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

    def __getitem__(self, index):
        if type(index) is tuple:
            return self._getitem(self, index)
        else:
            return super().__getitem__(index)

    def __setitem__(self, index, value):
        # coerce index to list
        if not hasattr(index, '__iter__'):
            index = [index]
        index = list(index)
        # fill out implicit arguments
        while len(index) <= len(self.shape):
            index.append(slice(None))
        for i, v in enumerate(index):
            if isinstance(v, int):
                v = slice(v, v+1)
                index[i] = v
        # assign to value
        indices = [s.indices(n) for s, n in zip(index, self.shape)]
        for idx in iteriters(*[range(start, stop, step) for start, stop, step in indices]):
            self[idx[:-1]][idx[-1]] = value

    def _getitem(self, matrix, index):
        if len(index) == 1:
            out = matrix.__getitem__(index[0])
            return out[0] if len(out) == 1 else out
        else:
            return self._getitem(transpose(matrix.__getitem__(index[0])), index[1:])

    @property
    def shape(self):
        shape = []
        item = self
        while isinstance(item, list):
            shape.append(len(item))
            item = item[0] if len(item) > 0 else None
        return tuple(shape)

    @property
    def size(self):
        out = 1
        for s in self.shape:
            out *= s
        return out
 
