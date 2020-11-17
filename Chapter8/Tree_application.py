# -*-coding:UTF-8 -*-

"""
树的应用函数

代码段8-23 : 用于打印先序遍历的缩进版本的高效递归(preorder_indent方法)
代码段8-24 : 打印先序遍历和缩进带序号标记版本(preorder_label方法)
代码段8-25 : 输出树的附加说明字符串表示函数(parenthesize方法)
代码段8-26 : 树的磁盘空间的递归计算(disk_space方法)
"""

from .Tree_abc import BaseTree


def preorder_indent(T: "BaseTree", p: "BaseTree.Position", d: int):
    """打印先序遍历的缩进版本"""
    print(2 * d * " " + str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d + 1)


def preorder_label(T: "BaseTree", p: "BaseTree.Position", d: int, path: list):
    """打印先序遍历和缩进带序号标记版本"""
    label = ".".join(str(j + 1) for j in path)
    print(2 * d * " " + label, p.element())
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d + 1, path)
        path[-1] += 1
    path.pop()


def parenthesize(T: "BaseTree", p: "BaseTree.Position"):
    """输出树的附加说明字符串表示函数"""
    print(p.element(), end="")
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = " (" if first_time else ", "
            print(sep, end="")
            first_time = False
            parenthesize(T, c)
        print(")", end="")


def disk_space(T: "BaseTree", p: "BaseTree.Position"):
    """树的磁盘空间的递归计算

    假设每个树元素的space()方法给出在这个位置的本地控件使用情况
    """
    subtotal = p.element().space()
    for c in T.children(p):
        subtotal += disk_space(T, c)
    return subtotal
