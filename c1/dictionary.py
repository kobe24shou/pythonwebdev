#!/usr/bin/env python
# -*-coding:utf-8-*-

# 字典 代表一个键值 存储库，有点像映射表 ，给定一个key ，可以在字典对象中搜索该键 对应的值
dict1 = {'Language': 'English', 'Title': 'Python book', 'Pages': 450}
print dict1['Title']									# 读取元素

dict1['Date'] = '2002-10-30'							# 直接通过下标新增字典内容
print dict1

dict1['Language'] = 'Chinese'						# 直接通过下标更新字典内容
print dict1

dict2 = {'Language': 'English', 'Language':'Chinese'}
print dict2

dict1 = {'Language': 'English', 'Title': 'Python book', 'Pages': 450}
print dict1.get('Title', 'Todo')					# 读取元素
print dict1.get('Author', 'Anonymous')			# 读取不存在的键
print dict1.pop('Language')							# pop
print dict1										# 检查pop后的字典内容

dict2={'Author':'David', 'Price':32.00, 'Pages':409 }
dict1.update(dict2)								# 合并字典
print dict1
print dict1.values()								# 获取值列表

