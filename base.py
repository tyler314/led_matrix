"""Parent class."""


# --- import -------------------------------------------------------------------------------------


import copy


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
            new = []
            for _ in range(s):
                new.append(copy.copy(lis))
            lis = new
        self._shape = shape
        list.__init__(self, lis)

    def __getitem__(self, index):
        if not hasattr(index, '__iter__'):
            return super().__getitem__(index)
        else:
            out = self
            for i in index:
                out = out[i]
            return out

    def __setitem__(self, index, value):
        # case of single integer
        if isinstance(index, int):
            return super().__setitem__(index, value)
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
        # for each
        indices = [s.indices(n) for s, n in zip(index, self.shape)]
        ranges = [range(start, stop, step) for start, stop, step in indices]
        for idx in iteriters(*ranges):
            self[idx[:-1]][idx[-1]] = value

    @property
    def shape(self):
        return self._shape
        shape = []
        item = self
        while isinstance(item, list):
            shape.append(len(item))
            item = item[0] if len(item) > 0 else None
        return tuple(shape)

    @property
    def size(self):
        if not self:
            return 0
        out = 1
        for s in self.shape:
            out *= s
        return out
