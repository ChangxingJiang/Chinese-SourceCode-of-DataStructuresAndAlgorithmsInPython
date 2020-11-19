# -*-coding:UTF-8 -*-

"""
使用基于数组的堆实现的适应性优先级队列（非继承的）
"""


class MyHeapq():
    """使用基于数组的堆实现的适应性优先级队列"""

    # -------------------- 嵌套的定位器类 --------------------
    class _Item:
        """轻量的、嵌套的元组类"""
        __slots__ = "key", "value"

        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __lt__(self, other):
            return self.key < other.key

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

    def _bubble(self, j):
        """j位置改变后恢复heap-order属性"""
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    # -------------------- 公有方法 --------------------
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
        token = self._Item(key, value)
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

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

    def update(self, j, newkey, newval):
        """更新优先级队列中指定位置的键值"""
        if not 0 <= j < len(self):
            raise ValueError("Invalid locator")
        self._data[j].key = newkey
        self._data[j].value = newval
        self._bubble(j)

    def remove(self, j):
        """移除优先级队列中指定位置的键值"""
        if not 0 <= j < len(self):
            raise ValueError("Invalid locator")
        if j == len(self) - 1:
            item = self._data.pop()
        else:
            self._swap(j, len(self) - 1)
            item = self._data.pop()
            self._bubble(j)
        return item.key, item.value

    def is_empty(self):
        """如果优先级队列为空则返回True"""
        return len(self) == 0
