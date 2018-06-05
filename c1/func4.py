#!/usr/bin/env python
# -*-coding:utf-8-*-
# 匿名函数: 指一类无须定义标识符（函数名）的函数或子程序，一般用于只在代码中存在一次函数引用的场合

import datetime


def namedFunc(a):
    return "I'm named function with param %s" % a


def call_func(func, param):
    print(datetime.datetime.now())   # datetime.datetime.now() 获取系统的当前时间
    print(func(param))
    print("")


if __name__ == '__main__':
    call_func(namedFunc, 'hello')
    call_func(lambda x: x * 2, 9)
    call_func(lambda y: y * y, -4)
