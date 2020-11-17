# -*-coding:UTF-8 -*-

"""
树的抽象基类

代码段8-1 : 嵌套的树的节点类 + 子类必须重写的抽象方法
代码段8-2 : 抽象基类的一些具体方法
代码段8-3 : 计算树的深度(depth方法)
代码段8-5 : 计算以p节点为根节点的子树的高度(_height方法)
代码段8-6 : 计算整个树或者一个给定位置作为根节点的子树的高度(height方法)
代码段8-16 : 返回基于树节点列表的迭代器(__iter__方法)
代码段8-17 : 树的先序遍历(preorder方法)
代码段8-18 : 返回树的所有节点的方法默认使用先序遍历(positions方法)
代码段8-19 : 树的后续遍历(postorder方法)
代码段8-20 : 树的广度优先遍历(breadthfirst方法)

修改说明:
1. 书中使用NotImplementedError来定义抽象基类，这里改为使用更正式的Python的abc模块
2. 书中类名为Tree，这里为了更清楚地区分抽象基类而命名为BaseTree
"""

from abc import ABCMeta
from abc import abstractmethod


class BaseTree(metaclass=ABCMeta):
    """树结构的抽象基类"""

    # -------------------- 嵌套的树的节点类 --------------------
    class Position(metaclass=ABCMeta):
        """树中节点的抽象基类"""

        @abstractmethod
        def element(self):
            """返回节点的值"""

        @abstractmethod
        def __eq__(self, other):
            """如果节点在树中的位置相同则返回True"""

        def __ne__(self, other):
            """如果节点在树中的位置不同则返回True"""
            return not (self == other)

    # -------------------- 子类必须重写的抽象方法 --------------------
    @abstractmethod
    def root(self):
        """返回树的根节点（若空树则返回None）"""

    @abstractmethod
    def parent(self, p):
        """返回节点p的父节点（若p节点为根节点则返回None）"""

    @abstractmethod
    def num_children(self, p):
        """返回节点p的子节点数量"""

    @abstractmethod
    def children(self, p):
        """迭代返回节点p的子节点"""

    @abstractmethod
    def __len__(self):
        """返回树的节点总数"""

    # -------------------- 抽象基类的一些具体方法 --------------------
    def is_root(self, p):
        """如果p节点为树的根节点则返回True"""
        return self.root() == p

    def is_leaf(self, p):
        """如果p节点为树的叶子节点则返回True"""
        return self.num_children(p) == 0

    def is_empty(self):
        """如果树为空则返回True"""
        return len(self) == 0

    # -------------------- 树的遍历方法 --------------------
    def preorder(self):
        """返回先序遍历树中所有节点的迭代器"""
        if not self.is_empty:
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """返回先序遍历以p为根节点的子树中所有节点的迭代器"""
        yield p  # 首先访问子树的根节点
        for c in self.children(p):  # 访问子树根节点的每个孩子节点
            for other in self._subtree_preorder(c):  # 对孩子节点的每一个节点进行先序遍历
                yield other  # 将结果yield到当前方法

    def postorder(self):
        """返回后序遍历树中所有节点的迭代器"""
        if not self.is_empty:
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """返回后序遍历以p为根节点的子树中所有节点的迭代器"""
        for c in self.children(p):  # 访问子树根节点的每个孩子节点
            for other in self._subtree_postorder(c):  # 对孩子节点的每一个节点进行后序遍历
                yield other  # 将结果yield到当前方法
        yield p  # 首先访问子树的根节点

    def breadthfirst(self):
        """返回广度优先遍历树中所有节点的迭代器"""
        if not self.is_empty():
            fringe = LinkedQueue()  # 记录还未yield的节点
            fringe.enqueue(self.root())  # 从根节点开始遍历
            while not fringe.is_empty():
                p = fringe.dequeue()  # 移除队列最前面的节点
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)  # 将当前节点的孩子节点添加到队列末尾

    def positions(self):
        """返回树的所有节点

        默认使用先序遍历返回结果
        """
        return self.preorder()

    def __iter__(self):
        """返回包含树中所有节点的迭代器"""
        for p in self.positions():  # 使用positions()方法的顺序
            yield p.element()

    # -------------------- 计算树的深度和高度的方法 --------------------
    def depth(self, p):
        """返回节点p的深度"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        """返回以p节点为根节点的子树的高度"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        """返回以p节点为根节点的子树的高度

        如果p为None，则返回整个树的高度
        """
        if p is None:
            p = self.root()
        return self._height(p)
