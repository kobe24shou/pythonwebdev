#!/usr/bin/env python
# -*-coding:utf-8-*-

tuple1 = ('you', 456, 'English', 9.34)				# 定义 用圆括号表示，不同元素之间用逗号隔开
print tuple1[2]								# 读取元素
print tuple1[1:]								# 截取子元组

# tuple1[2]='France'							#错误！不能修改元组内容
# 元组 的大小和其中的元素在初始化后不能修改，元组比可修改的list 操作速度快 
# 如果需要定义一个值是常量值，并且唯一要用它做的是不断的读取 --》这是元组的长度
tuple2 = (3, 'you and me')
tuple1 = tuple1 + tuple2						# 可以对元组变量重新赋值

print tuple1
print len(tuple2)								# 用函数len()获得元组长度
