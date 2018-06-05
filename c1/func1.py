#!/usr/bin/env python
# -*-coding:utf-8-*-

# 函数参数定义默认值
def sum(x, y=10):
    return x + y


if __name__ == '__main__':
    print("return of sum(2, 3):", sum(2, 3))
    print("return of sum(-4):", sum(-4))