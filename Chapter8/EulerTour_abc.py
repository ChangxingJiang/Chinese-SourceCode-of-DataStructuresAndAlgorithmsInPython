# -*-coding:UTF-8 -*-

"""
欧拉遍历基类的框架

代码段8-28 : 欧拉遍历基类的框架

修改说明:
1. 使用@property装饰器装饰的数据成员_tree
"""


class EulerTour:
    """欧拉遍历的抽象基类

    具体类可以重写_hook_previsit和_hook_postvisit方法
    """

    def __init__(self, tree):
        """准备对目标树执行欧拉遍历"""
        self._tree = tree

    @property
    def tree(self):
        """返回正在被遍历的树"""
        return self._tree

    def execute(self):
        """从根节点开始执行欧拉遍历"""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])  # 启动递归

    def _tour(self, p, d, path):
        """对以节点p为根节点的子树执行欧拉遍历

        :param p: 当前子树的根节点p
        :param d: p节点的深度
        :param path: 从根节点到节点p的节点序号列表
        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)  # 添加当前层的节点序数
        for c in self._tree.children(p):
            results.append(self._tour(c, d + 1, path))  # 递归子树
            path[-1] += 1  # 更新节点序号
        path.pop()  # 移除当前层的节点序数
        return self._hook_postvisit(p, d, path, results)

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass
