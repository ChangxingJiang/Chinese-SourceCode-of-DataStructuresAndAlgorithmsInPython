# -*-coding:UTF-8 -*-

"""
算术表达式树

代码段8-35 : 算术表达式树类Part1
代码段8-37 : 算术表达式树类的结果计算(evaluate方法)
代码段8-38 : 依据字符串格式的算术表达式生成算术表达式树实例(build_expression_tree方法)
"""

from .LinkedBinaryTree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    """算术表达式树类"""

    def __init__(self, token, left=None, right=None):
        """创建算术表达式实例"""
        super().__init__()  # 实例化二叉树
        if not isinstance(token, str):
            raise TypeError("Token must be a string")
        self._add_root(token)
        if left is not None:
            if token not in "+-*x/":
                raise ValueError("Token must be valid operator")
        self._attach(self.root(), left, right)

    def __str__(self):
        """返回字符串表示的算术表达式"""
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return "".join(pieces)

    def _parenthesize_recur(self, p, result):
        """添加节点p中的表达式到result列表中"""
        if self.is_leaf(p):
            result.append(str(p.element()))  # 将叶子节点的数字转换为字符串
        else:
            result.append("(")
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)
            result.append(")")

    def evaluate(self):
        """返回算术表达式的计算结果"""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """返回以节点p为根节点的子树的算术表达式的结果"""
        if self.is_leaf(p):
            return float(p.element())  # 将叶子节点的数值转换为float格式
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == "+":
                return left_val + right_val
            elif op == "-":
                return left_val - right_val
            elif op == "/":
                return left_val / right_val
            else:
                return left_val * right_val


def build_expression_tree(tokens):
    """依据字符串格式的算术表达式生成算术表达式树实例"""
    stack = []
    for t in tokens:
        if t in "+-*x/":
            stack.append(t)
        elif t not in "()":
            stack.append(ExpressionTree(t))
        elif t == ")":
            right = stack.pop()
            op = stack.pop()
            left = stack.pop()
            stack.append(ExpressionTree(op, left, right))
    return stack.pop()
