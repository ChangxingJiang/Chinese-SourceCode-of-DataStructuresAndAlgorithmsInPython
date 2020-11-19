# -*-coding:UTF-8 -*-

"""
使用排序列表实现的优先级队列

代码段9-2 : 使用排序列表实现的优先级队列
"""
from .PriorityQueueBase_abc import PriorityQueueBase


class UnsortedPriorityQueue(PriorityQueueBase):
    """使用排序列表实现的最小值优先级队列类"""

    def __init__(self):
        """创建优先级队列实例"""
        self._data = PositionList()

    def __len__(self):
        """返回优先级队列的元素数量"""
        return len(self._data)

    def add(self, key, value):
        """添加键值对"""
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """返回优先级队列的最小值"""
        if self.is_empty():
            raise ValueError("Priority queue is Empty")
        p = self._data.first()
        item = p.element()
        return item.key, item.value

    def remove_min(self):
        """移除优先级队列的最小值"""
        if self.is_empty():
            raise ValueError("Priority queue is Empty")
        item = self._data.delete(self._data.first())
        return item.key, item.value
