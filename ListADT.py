import ctypes

class ArrayList:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._Array  = self.makeArray(self._capacity)

    def __getitem__(self, item):
        return self._Array[item]

    def __setitem__(self, key, value):
        assert key <= self._n
        self._Array[key] = value


    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 *(self._capacity))
        self._Array[self._n] = obj
        self._n += 1


    def _resize(self, c):
        B = self.makeArray(c)
        for i in range(self._n):
            B[i] = self._Array[i]
        self._Array = B
        self._capacity = c


    def _pop(self, k):
        assert k <= self._n
        item  = self._Array[k]
        self._Array[self._n] = None
        self._n -= 1
        return self.__getitem__(k)


    def makeArray(self, c):
        return (c * ctypes.py_object)()

list_a = ArrayList()
list_a.append(45)
list_a.append(569)
list_a.append(56)
list_a.append(67)
list_a.append('df')
print list_a._pop(2)
print list_a._pop(0)
# print list_a.__getitem__(1)
list_a.__setitem__(0, 90)
print list_a._Array
print  list_a.__dict__