# -*-coding:UTF-8 -*-

"""
优先级队列的抽象基类

代码段9-1 : 优先级队列的抽象基类

修改说明:
1. 使用更正式的Python的abc模块
2. 使用@property和@setter装饰器装饰的方法访问_Item类的部分数据成员，以避免直接访问非公开的数据成员
3. 将__len__作为抽象方法添加到抽象基类中，以避免is_empty方法报错
"""

from abc import ABCMeta
from abc import abstractmethod


class PriorityQueueBase(metaclass=ABCMeta):
    """优先级队列的抽象基类"""

    class _Item:
        """轻量的、嵌套的元组类"""
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        @property
        def key(self):
            return self._key

        @key.setter
        def key(self, key):
            self._key = key

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

        def __lt__(self, other):
            return self.key < other.key

    @abstractmethod
    def __len__(self):
        """返回优先级队列的元素数量"""
        pass

    def is_empty(self):
        """如果优先级队列为空则返回True"""
        return len(self) == 0
