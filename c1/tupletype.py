#!/usr/bin/env python
# -*-coding:utf-8-*-

# 元组 类型


tuple1 = ('you', 456, 'English', 9.34)				# 定义
print(tuple1[2])							# 读取元素
print(tuple1[1:])								# 截取子元组

# tuple1[2]='France'							# 错误！不能修改元组内容

tuple2 = (3, 'you and me')
tuple1 = tuple1 + tuple2						# 可以对元组变量重新赋值
print(tuple1)
print(len(tuple2))							# 用函数len()获得元组长度


# list 类型

myList = ['you', 456, 'English', 9.34]				# 定义
print(myList[2]	)							# 读取元素
print(myList[1:])								# 截取子列表

myList[2] = 'France'							# 可以修改内容
print(myList)
print(len(myList))								# 用函数len()获得列表长度

# numList = [2, 8, 16, 1, -6, 52, -1]		    # 定义
# print(sorted(myList))							# 排序
# print(myList)								    # sorted后myList本身并不改变
# print(sum(numList))							# 求和


numList = [2, 8, 16, 8, -6, 52, -1]				# 定义
print(numList.count(8))							# count

numList.insert(1, 9)							# 在位置1增加元素9
print(numList)

# set 类型
print("set 类型==============================>")
sample1 = set('understand')					#用string初始化set
print(sample1)

myList = [ 4, 6, -1.1, 'English', 0, 'Python']
sample2 = set(myList)							#用list初始化set
print(sample2)

sample3 = frozenset(myList)					#初始化frozenset
print(sample3)


myList = [ 4, 6, -1.1, 'English', 0, 'Python']
sample2 = set(myList)							#初始化set
sample3 = frozenset([ 6, 'English', 9])				#初始化frozenset

print(6 in sample2)							#判断包含关系
print(sample2 >= sample3)						#判断子集关系
print(sample2 - sample3)						#差运算
print(sample2 & sample3)						#交运算

sample3 |= sample2							#可以对frozenset执行 |= 重新赋值
print(sample3)


sample2 = set([ 4, 6, -1.1, 'English', 0, 'Python'])		#初始化set
sample2.add('China')							#增加元素
print(sample2)
sample2.update('France')						#用序列更新
print(sample2)
sample2.remove(-1.1)							#删除元素
print(sample2)
sample3 = frozenset([ 6, 'English', 9])				#初始化frozenset
# sample3.add('China')							#错误，frozenset无法更新

# 字典 类型 类似映射表
print("dit  字典========================>")
dict1 = {'Language': 'English', 'Title': 'Python book', 'Pages': 450}

print(dict1['Title'])									#读取元素

dict1['Date'] = '2002-10-30'							#直接通过下标新增字典内容
print(dict1)

dict1['Language'] = 'Chinese'						#直接通过下标更新字典内容
print(dict1)

dict2 = {'Language': 'English', 'Language':'Chinese'}
print(dict2)


dict1 = {'Language': 'English', 'Title': 'Python book', 'Pages': 450}

print(dict1.get('Title', 'Todo'))					# 读取元素
print(dict1.get('Author', 'Anonymous'))			# 读取不存在的键
print(dict1.pop('Language'))							# pop
print(dict1)										# 检查pop后的字典内容

dict2 = {'Author':'David', 'Price':32.00, 'Pages': 409}
dict1.update(dict2)								# 合并字典
print(dict1)

print(dict1.values())								# 获取值列表
