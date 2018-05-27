#!/usr/bin/env python
# -*-coding:utf-8-*-

# list 列表用中括号[] 表示，不同元素之间以逗号隔开
# list 的大小和其中 的元素 在初始化后可以被再次修改 ，这是list 和元组 主要区别
# 如果 定义了一组值，并且在之后 需要不断对其进行增 删 改 查等操作，就应该使用list

myList = ['you', 456, 'English', 9.34]				# 定义

print myList[2]								# 读取元素
print myList[1:]								# 截取子列表

myList[2] = 'France'							# 可以修改内容
print myList
print len(myList)								# 用函数len()获得列表长度

numList = [2, 8, 16, 1, -6, 52, -1]					# 定义
print sorted(myList)							# 排序
print myList								# sorted后myList本身并不改变
print sum(numList)							# 求和


numList = [2, 8, 16, 8, -6, 52, -1]					#定义
print numList.count(8)							# count 计算对象在列表中出现的次数
numList.insert(1, 9)							# 在位置1增加元素9
print numList
