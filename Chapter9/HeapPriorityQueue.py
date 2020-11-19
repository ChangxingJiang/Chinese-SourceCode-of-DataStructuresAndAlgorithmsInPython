# -*-coding:UTF-8 -*-

"""
使用基于数组的堆实现的优先级队列

代码段9-4 : 使用基于数组的堆实现的优先级队列Part1(非空开方法)
代码段9-5 : 使用基于数组的堆实现的优先级队列Part1(空开方法)
代码块9-6 : 支持对给定元祖序列实现线性复杂度的优先级队列构建的构造方法

修改说明:
1. 将部分静态方法增加@staticmethod装饰器
"""

from .PriorityQueueBase_abc import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    """使用排序列表实现的最小值优先级队列类"""

    # -------------------- 非公开方法 --------------------
    @staticmethod
    def _parent(j):
        return (j - 1) // 2

    @staticmethod
    def _left(j):
        return 2 * j + 1

    @staticmethod
    def _right(j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """交换节点i和节点j"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """堆向上冒泡"""
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # 递归继续向上冒泡

    def _downheap(self, j):
        """堆向下冒泡"""
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)  # 递归继续向下冒泡

    # -------------------- 公开方法 --------------------
    def __init__(self, contents=()):
        """创建优先级队列实例"""
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self) - 1)
        for j in range(start, -1, -1):
            self._downheap(j)

    def __len__(self):
        """返回优先级队列的元素数量"""
        return len(self._data)

    def add(self, key, value):
        """添加键值对"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        """返回优先级队列的最小值"""
        if self.is_empty():
            raise ValueError("Priority queue is Empty")
        item = self._data[0]
        return item.key, item.value

    def remove_min(self):
        """移除优先级队列的最小值"""
        if self.is_empty():
            raise ValueError("Priority queue is Empty")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item.key, item.value
