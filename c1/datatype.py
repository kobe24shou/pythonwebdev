#!/usr/bin/env python
# -*-coding:utf-8-*-

a = "Hello, I like Python Web Practice!"  # 字符串类型
b = a[1]
b = a[7:13]

print(a[:13]) # 字符串截取
print(a[14:])
print("like" in a)  # 字符串是否存在
print(a + "!!")   # 字符串拼接
print(a)
print("ABC" * 3)   # + 号 字符串连乘

c = [2, 4, "apple", 5]
print(c[1:])
print(b + c[2])

# 内置函数
a = [56, 2, 1, 893, -0.4]				    # 列表类型
b = len(a)									# 结果为 5
b = max(a)									# 结果为 893
b = min(a)									# 结果为 -0.4
print(list(reversed(a)))
print(sorted(a))
print("string 类型=====>")									# 打印字符串
# string 类型
str1 = "Hello, World!"							# 普通字符串
str2 = u"Hello, I’m Unicode	!"					# Unicode字符串
str3 = u"你好，世界！"						# Unicode字符串
print(str2)									# 打印字符串

str1 = "Hello, World!"					# 定义字符串
print(str1[5])							# 读取位置为2的元素				#位置为2的元素是逗号’,’
print(str1[7:])							# 读取位置从7到最后的子字符串


str1 = str2 = "Hello, World!"					#定义字符串
str1 = str1 + " I like Python!"					#尾部附加内容
print(str1)
str1 = str1[:6] + str1[-8:]						#删除中间的部分内容
print(str1)


charA = 65
charB = 66

print(u"ASCII码65代表：%c" % charA)
print(u"ASCII码%d代表：B" % charB)

print("%#x" % 108)						         # 十六进制数字
print('%E' % 1234.567890)					     # 科学计数法
print('Host: %s\tPort: %d' % ('python', 80))			# 多个参数
print('MM/DD/YY = %02d/%02d/%d' % (2, 1, 95))	  # 数字前补零

str = "hello world"							# 定义
print(str.title())							# 标题化
print(str.split())							# 切片

print("Hi, \nToday is Friday.")
print(r"Hi, \ntoday is Friday.")				# 用’r’禁用转义字符
