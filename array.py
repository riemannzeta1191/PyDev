import ctypes
from collections import defaultdict
# Array = ctypes.
# slots = Array()
# for i in range(5):
#     slots[i] = i
# slots[2] = None
# print  list(slots)

"""
Array ADT using ctypes module
"""

class Array():

    def __init__(self, size):
        self._size = size
        PyArray = ctypes.py_object * 5
        self._element = PyArray()
        # self.clear(None)


    def __len__(self):
        return self._size

    def __getitem__(self, item):
        return self._element[item]

    def __setitem__(self, index, value):
        assert index < len(self)
        self._element[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._element = value



    def __iter__(self):
        return  _ArrayIterator(self._element)

class _ArrayIterator:
    def __init__(self, theArray):
        self._array = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._array):
            entry = self._array[self._curNdx]
            self._curNdx +=1
        else:
            raise StopIteration


A = Array(10)
A.clear(defaultdict())
A.__setitem__(0,12)
A.__setitem__(1,19)
A.__setitem__(1,None)
print A.__dict__,A[0],A[1]

