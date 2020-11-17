# -*-coding:UTF-8 -*-

"""
基于链式存储结构的二叉树类

代码段8-8 : 嵌套的二叉树的节点类及相关私有方法
代码段8-9 : 二叉树的公开访问方法
代码段8-10 : 二叉树的非公开更新方法Part1
代码段8-11 : 二叉树的非公开更新方法Part2

修改说明:
1. 书中使用NotImplementedError来定义抽象基类，这里改为使用更正式的Python的abc模块
2. 使用@property和@setter装饰器装饰的方法访问_Node类、Position类和LinkedBinaryTree类中的部分数据成员，以避免直接访问非公开的数据成员
"""

from .BinaryTree_abc import BaseBinaryTree


class LinkedBinaryTree(BaseBinaryTree):
    """基于链式存储结构的二叉树类"""

    class _Node:
        """轻量的、私有的节点类"""

        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

        @property
        def element(self):
            return self._element

        @element.setter
        def element(self, element):
            self._element = element

        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, parent):
            self._parent = parent

        @property
        def left(self):
            return self._left

        @left.setter
        def left(self, left):
            self._left = left

        @property
        def right(self):
            return self._right

        @right.setter
        def right(self, right):
            self._right = right

    class Position(BaseBinaryTree.Position):
        """封装的、公开的节点类（用于封装_Node类）"""

        def __init__(self, container, node):
            """不应让用户直接调用构造函数"""
            self._container = container
            self._node = node

        def element(self):
            """返回节点的值"""
            return self.node.element

        def __eq__(self, other):
            """如果节点在树中的位置相同则返回True"""
            return type(other) is type(self) and other.node is self.node

        @property
        def container(self):
            return self._container

        @property
        def node(self):
            return self._node

    def _validate(self, p):
        """如果节点存在则返回被封装的节点对象"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p.container is not self:
            raise ValueError("p does not belong to this container")
        if p.node.parent is p.node:  # 弃用节点的规定
            raise ValueError("p is no longer valid")
        return p.node

    def _make_position(self, node):
        """依据给定节点返回封装后的节点对象"""
        return self.Position(self, node) if node is not None else None

    # -------------------- 基于链式存储结构的二叉树类的构造器 --------------------
    def __init__(self):
        """构造一个空的二叉树实例"""
        self._root = None
        self._size = 0

    # -------------------- 公开访问方法 --------------------
    def __len__(self):
        """返回二叉树的节点总数"""
        return self._size

    def root(self):
        """返回二叉树的根节点（若空树则返回None）"""
        return self._make_position(self._root)

    def parent(self, p):
        """返回节点p的父节点（若p节点为根节点则返回None）"""
        node = self._validate(p)
        return self._make_position(node.parent)

    def left(self, p):
        """返回节点p的左子节点（如果节点p没有左子节点则返回None）"""
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self, p):
        """返回节点p的右子节点（如果节点p没有右子节点则返回None）"""
        node = self._validate(p)
        return self._make_position(node.right)

    def num_children(self, p):
        """返回节点p的子节点数量"""
        node = self._validate(p)
        count = 0
        if node.left is not None:  # 如果左子节点存在
            count += 1
        if node.right is not None:  # 如果右子节点存在
            count += 1
        return count

    @property
    def root_node(self):
        return self._root

    @root_node.setter
    def root_node(self, node):
        self._root = node

    # -------------------- 非公开更新方法 --------------------
    def _add_root(self, e):
        """为空树创建值为e的根节点，并返回根节点对象

        如果树是非空的则抛出ValueError异常
        """
        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """为p节点创建值为e的左子节点，并返回新的左子节点对象

        如果p节点不存在或p节点已经存在左子节点，则抛出TypeError或ValueError异常
        """
        node = self._validate(p)
        if node.left is not None:
            raise ValueError("Left child exists")
        self._size += 1
        node.left = self._Node(e, node)
        return self._make_position(node.left)

    def _add_right(self, p, e):
        """为p节点创建值为e的右子节点，并返回新的右子节点对象

        如果p节点不存在或p节点已经存在右子节点，则抛出TypeError或ValueError异常
        """
        node = self._validate(p)
        if node.right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node.right = self._Node(e, node)
        return self._make_position(node.right)

    def _replace(self, p, e):
        """将p节点的值替换为e，并返回之前的值"""
        node = self._validate(p)
        old = node.element
        node.element = e
        return old

    def _delete(self, p):
        """删除节点p，如果它有一个孩子节点则用它的孩子节点代替它

        返回节点p的值
        如果节点p不存在或节点p有两个孩子节点，则抛出TypeError或ValueError异常
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        child = node.left if node.left else node.right  # child可能为空
        if child is not None:
            child.parent = node.parent  # 令孩子节点的祖父节点成为其父节点
        if node is self._root:
            self._root = child  # 如果节点p为根节点，则其孩子节点成为根节点
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self._size -= 1
        node.parent = node  # 弃用节点的规定
        return node.element

    def _attach(self, p, t1, t2):
        """将树t1、t2分别连接为节点p的左右子树，并将t1和t2重置为空树

        如果节点p所在的树、t1、t2的类型不同，则抛出TypeError异常
        如果节点p不存在或节点p不是叶子节点，则抛出TypeError或ValueError异常
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):  # 三个树必须拥有相同的类型
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # 将t1连接为node的左子树
            t1.root_node.parent = node
            node.left = t1.root_node
            t1.root_node = None  # 将t1实例设置为空
            t1._size = 0
        if not t2.is_empty():  # 将t2连接为node的右子树
            t2.root_node.parent = node
            node.right = t2.root_node
            t2.root_node = None  # 将t2实例设置为空
            t2._size = 0
