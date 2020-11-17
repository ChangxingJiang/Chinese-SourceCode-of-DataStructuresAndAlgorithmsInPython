# -*-coding:UTF-8 -*-

"""
二叉树的欧拉遍历基类的框架

代码段8-33 : 二叉树的欧拉遍历基类
"""

from .EulerTour_abc import EulerTour


class BinaryEulerTour(EulerTour):
    """二叉树的欧拉遍历的抽象基类

    增加了可以重写的_hook_invisit方法，该方法将在左子树访问后，右子树访问前被调用。

    说明：右子树的节点序数恒为1，无论是否有左子树
    """

    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)  # 先序遍历
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d + 1, path)
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d + 1, path)
            path.pop()
        return self._hook_postvisit(p, d, path, results)

    def _hook_invisit(self, p, d, path):
        pass
