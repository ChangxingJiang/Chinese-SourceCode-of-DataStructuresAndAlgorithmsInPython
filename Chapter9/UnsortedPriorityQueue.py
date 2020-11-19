# -*-coding:UTF-8 -*-

"""
使用未排序列表实现的优先级队列

代码段9-2 : 使用未排序列表实现的优先级队列
"""
from .PriorityQueueBase_abc import PriorityQueueBase


class UnsortedPriorityQueue(PriorityQueueBase):
    """使用未排序列表实现的最小值优先级队列类"""

    def __init__(self):
        """创建优先级队列实例"""
        self._data = PositionList()

    def _find_min(self):
        """返回队列中的最小值的位置"""
        if self.is_empty():
            raise ValueError("Priority queue is Empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __len__(self):
        """返回优先级队列的元素数量"""
        return len(self._data)

    def add(self, key, value):
        """添加键值对"""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """返回优先级队列的最小值"""
        p = self._find_min()
        item = p.element()
        return item.key, item.value

    def remove_min(self):
        """移除优先级队列的最小值"""
        p = self._find_min()
        item = self._data.delete(p)
        return item.key, item.value
