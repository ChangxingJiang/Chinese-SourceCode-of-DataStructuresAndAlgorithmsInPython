# -*-coding:UTF-8 -*-

"""
使用基于数组的堆实现的适应性优先级队列

代码段9-8 : 一个可适应性优先级队列的实现Part1
代码段9-9 : 一个可适应性优先级队列的实现Part2

修改说明:
1. 使用@property和@setter装饰器装饰的方法访问Locator类的部分数据成员，以避免直接访问非公开的数据成员
"""

from .HeapPriorityQueue import HeapPriorityQueue


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """使用基于数组的堆实现的适应性优先级队列"""

    # -------------------- 嵌套的定位器类 --------------------
    class Locator(HeapPriorityQueue._Item):
        """作为公有接口的用户定位器"""
        __slots__ = "_index"

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

        @property
        def index(self):
            return self._index

        @index.setter
        def index(self, index):
            self._index = index

    # -------------------- 非公有方法 --------------------
    # 重写的节点交换方法
    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i].index = i
        self._data[j].index = j

    def _bubble(self, j):
        """j位置改变后恢复heap-order属性"""
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    # -------------------- 公有方法 --------------------
    def add(self, key, value):
        """添加键值对"""
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        """更新优先级队列中指定位置的键值"""
        j = loc.index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        loc.key = newkey
        loc.value = newval
        self._bubble(j)

    def remove(self, loc):
        """移除优先级队列中指定位置的键值"""
        j = loc.index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        if j == len(self) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self) - 1)
            self._data.pop()
            self._bubble(j)
        return loc.key, loc.value
