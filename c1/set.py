#!/usr/bin/env python
# -*-coding:utf-8-*-

# 集合表示相互之间无序 的一组对象
# 集合分为两类 普通集合（在初始化后支持并集，交集，补集等运算） 和 不可变集合（初始化后就不能改变）

sample1 = set('understand')					# 用string初始化set
print sample1

myList = [ 4, 6, -1.1, 'English', 0, 'Python']
sample2 = set(myList)							# 用list初始化set=普通集合
print sample2

sample3 = frozenset(myList)					# 初始化 frozenset=不可变集合
print sample3

myList = [ 4, 6, -1.1, 'English', 0, 'Python']
sample2 = set(myList)							# 初始化set
sample3 = frozenset([ 6, 'English', 9])				# 初始化frozenset

print 6 in sample2							# 判断包含关系
print sample2 >= sample3						# 判断子集关系
print sample2 - sample3						# 差运算
print sample2 & sample3						# 交运算
sample3 |= sample2							# 可以对frozenset执行 |= 重新赋值
print sample3


sample2 = set([ 4, 6, -1.1, 'English', 0, 'Python'])		# 初始化set

sample2.add('China')							# 增加元素
print sample2

sample2.update('France')						# 用序列更新
print sample2

sample2.remove(-1.1)							# 删除元素
print sample2

sample3 = frozenset([ 6, 'English', 9])				# 初始化frozenset

# sample3.add('China')							# 错误，frozenset无法更新
