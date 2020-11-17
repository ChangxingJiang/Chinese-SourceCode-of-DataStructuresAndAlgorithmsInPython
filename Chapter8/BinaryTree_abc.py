# -*-coding:UTF-8 -*-

"""
二叉树的抽象基类

代码段8-7 : 二叉树扩展的抽象方法 + 二叉树抽象基类扩展的一些具体方法

修改说明:
1. 书中使用NotImplementedError来定义抽象基类，这里改为使用更正式的Python的abc模块
2. 书中类名为BinaryTree，这里为了更清楚地区分抽象基类而命名为BaseBinaryTree
"""

from abc import ABCMeta
from abc import abstractmethod

from .Tree_abc import BaseTree


class BaseBinaryTree(BaseTree, metaclass=ABCMeta):
    """二叉树结构的抽象基类"""

    # -------------------- 二叉树扩展的抽象方法 --------------------
    @abstractmethod
    def left(self, p):
        """返回节点p的左子节点（如果节点p没有左子节点则返回None）"""

    @abstractmethod
    def right(self, p):
        """返回节点p的右子节点（如果节点p没有右子节点则返回None）"""

    # -------------------- 二叉树扩展的一些具体方法 --------------------
    def sibling(self, p):
        """返回节点p的兄弟节点（如果没有兄弟节点则返回None）"""
        parent = self.parent(p)
        if parent is None:  # 如果parent为空则说明节点p为根节点
            return None  # 根节点没有兄弟节点
        else:
            if p == self.left(parent):
                return self.right(parent)  # 可能为空
            else:
                return self.left(parent)  # 可能为空

    def children(self, p):
        """迭代返回节点p的子节点"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # -------------------- 二叉树的遍历方法 --------------------
    def inorder(self):
        """返回中序遍历二叉树中所有节点的迭代器"""
        if not self.is_empty:
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """返回中序遍历以p为根节点的子二叉树中所有节点的迭代器"""
        if self.left(p) is not None:  # 如果左子树存在，遍历左子树
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p  # 在左右子树之间访问当前节点
        if self.right(p) is not None:  # 如果右子树存在，遍历右子树
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def positions(self):
        """返回树的所有节点

        默认使用中序遍历树的所有节点
        """
        return self.inorder()
