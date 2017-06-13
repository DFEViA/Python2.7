#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 6.6递归 函数调用自身
# 无穷递归


def recursion():
    return recursion()

# 6.6.1两个景点：阶乘和幂


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# 这就是定义的直接实现


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

# 6.6.2另一个经典：二元查找


def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        # 序列不存在要查找的元素跑出异常
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)

seq = [12, 54, 6, 21, 231, 1, 3, 456, 100]
seq.sort()
print seq
print search(seq, 6)
# print search(seq,7)
print 13 in seq
