# -*-coding:UTF-8 -*-

"""
欧拉遍历的应用

代码段8-29 : 打印先序遍历的缩进版本(preorder_indent函数)
代码段8-30 : 打印先序遍历和缩进带序号标记版本(preorder_label函数)
代码段8-31 : 输出树的附加说明字符串表示函数(parenthesize函数)
代码段8-32 : 树的磁盘空间的递归计算(disk_space函数)
"""

from .EulerTour_abc import EulerTour


def preorder_indent(T):
    """打印先序遍历的缩进版本"""

    class PreorderPrintIndentedTour(EulerTour):
        def _hook_previsit(self, p, d, path):
            print(2 * d * " " + str(p.element()))

    tour = PreorderPrintIndentedTour(T)
    tour.execute()


def preorder_label(T):
    """打印先序遍历和缩进带序号标记版本"""

    class PreorderPrintIndentedLabeledTour(EulerTour):
        def _hook_previsit(self, p, d, path):
            label = ".".join(str(j + 1) for j in path)
            print(2 * d * " " + label, p.element())

    tour = PreorderPrintIndentedLabeledTour(T)
    tour.execute()


def parenthesize(T):
    """输出树的附加说明字符串表示函数"""

    class ParenthesizeTour(EulerTour):
        def _hook_previsit(self, p, d, path):
            if path and path[-1] > 0:
                print(", ", end="")
            print(p.element(), end="")
            if not self.tree.is_leaf(p):
                print(" (", end="")

        def _hook_postvisit(self, p, d, path, results):
            if not self.tree.is_leaf(p):
                print(")", end="")

    tour = ParenthesizeTour(T)
    tour.execute()


def disk_space(T):
    """树的磁盘空间的递归计算

    假设每个树元素的space()方法给出在这个位置的本地控件使用情况
    """

    class DiskSpaceTour(EulerTour):
        def _hook_postvisit(self, p, d, path, results):
            return p.element().space() + sum(results)

    tour = DiskSpaceTour(T)
    return tour.execute()
