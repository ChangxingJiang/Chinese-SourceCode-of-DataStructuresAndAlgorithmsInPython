# -*-coding:UTF-8 -*-

"""
有序映射类

代码段10-8 : 有序映射类Part1
代码段10-9 : 有序映射类Part2
代码段10-10 : 有序映射类Part3
"""

from .MapBase_abc import MapBase


class SortedTableMap(MapBase):
    """有序映射类"""

    def _find_index(self, k, low, high):
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._table[mid].key:
                return mid
            elif k < self._table[mid].key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j].key != k:
            raise KeyError("Key Error: " + repr(k))
        return self._table[j].key

    def __setitem__(self, k, v):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j].key != k:
            self._table[j].value = v
        else:
            self._table.insert(j, self._Item(k, v))

    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j].key != k:
            raise KeyError("Key Error: " + repr(k))
        self._table.pop(j)

    def __iter__(self):
        for item in self._table:
            yield item.key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item.key

    def find_min(self):
        if len(self._table) > 0:
            return self._table[0].key, self._table[0].value
        else:
            return None

    def find_max(self):
        if len(self._table) > 0:
            return self._table[-1].key, self._table[-1].value
        else:
            return None

    def find_lt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            return self._table[j - 1].key, self._table[j - 1].value
        else:
            return None

    def find_le(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j].key == k:
            return self._table[j].key, self._table[j].value
        elif j > 0:
            return self._table[j - 1].key, self._table[j - 1].value
        else:
            return None

    def find_gt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j].key == k:
            j += 1
        if j < len(self._table):
            return self._table[j].key, self._table[j].value
        else:
            return None

    def find_ge(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            return self._table[j].key, self._table[j].value
        else:
            return None

    def find_range(self, start, stop):
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)
        while j < len(self._table) and (stop is None or self._table[j].key < stop):
            yield self._table[j].key, self._table[j].value
            j += 1
