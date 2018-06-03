#!/usr/bin/env python
# -*-coding:utf-8-*-
# 根据控制台输入数字的参数判断数值大小的程序

import sys
param = None   # 定义param 的初始值为空， 该变量用于在之后保存输入参数

if len(sys.argv) > 1:  # if 判断控制台是否有参数输入，如果有，则将第1个参数 转换位 int 类型并放入param变量中
    param = int(sys.argv[1])  # sys.argv 是一个系统list 变量
# int(sys.argv[1]) 将第1个输入参数从字符串类型转换到整型

if param is None:
    print("Alert")
    print("The param is not set")
elif param < -10:
    print("The param is small")
elif param > 10:
    print("the param is big")
else:
    print("the param is middle")

#  每个 if ，elif，else 块可以放入多条语句
#  运行方式 python ifexpress.py 3
