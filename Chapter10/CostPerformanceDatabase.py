# -*-coding:UTF-8 -*-

"""
一个使用有序映射维持最大值的类的实现

代码段10-11 : 一个使用有序映射维持最大值的类
"""

from .SortedTableMap import SortedTableMap


class CostPerformanceDatabase:

    def __init__(self):
        self._M = SortedTableMap()

    def best(self, c):
        return self._M.find_le(c)

    def add(self, c, p):
        other = self._M.find_le(c)
        if other is not None and other[1] >= p:
            return
        self._M[c] = p
        other = self._M.find_gt(c)
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)
