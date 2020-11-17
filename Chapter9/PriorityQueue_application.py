# -*-coding:UTF-8 -*-

"""
优先级队列的应用

代码段9-7 : 使用优先级队列排序（堆排序）
"""

from .HeapPriorityQueue import HeapPriorityQueue


def pq_sort(C):
    """使用优先级队列排序（堆排序）"""
    n = len(C)
    P = HeapPriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)
    for j in range(n):
        (k, v) = P.remove_min()
        C.add_last(v)
