# -*-coding:UTF-8 -*-

"""
二叉树遍历的应用

代码段8-34 : 计算坐标绘制二叉树图形布局(BinaryLayout类)
"""

from .BinaryEulerTour_abc import BinaryEulerTour


class BinaryLayout(BinaryEulerTour):
    """用于计算坐标绘制二叉树图形布局的类"""

    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)  # 依据序数计算x的坐标（中序遍历是严格的从左向右）
        p.element().setY(d)  # 依据深度计算y的坐标
        self._count += 1
