# -*-coding:UTF-8 -*-

"""
字典的抽象基类

代码段10-2 : 通过扩展MutableMapping抽象基类的字典的抽象基类
"""

from collections import MutableMapping


class MapBase(MutableMapping):
    """字典的抽象基类"""

    # -------------------- 嵌套的元组类 --------------------
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

        def __eq__(self, other):
            return self.key == other.key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self.key < other.key
