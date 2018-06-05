#!/usr/bin/env python
# -*-coding:utf-8-*-

myList = ['English', 'Chinese', 'Japanese', 'German', 'France']

#  逐个输出mylist 列表中的内容，知道列表长度为0
while len(myList) > 0:
    print("pop element out :", myList.pop())

#  while 判断为真， 执行下面的语句块
#  while 中expression 一直为真，则程序永远无法退出

myList = [ 'English', 'Chinese', 'Japanese', 'German', 'France' ]

#  for  in 是关键字  ，其中in 后面可以是序列，集合，迭代器等
for language in myList:
    print("Current element is :", language)

count = 0
# 变量 count 用于对循环体计数
while True:
    input1 = input("Enter quit: ")
    # check for valid passwd
    if input1 == "quit":
        break
    count = count + 1
    if count % 3 > 0:
        continue  # 是否是3 的倍数 ，如果不是则用 contiune 语句 继续循环
    print("Please input quit!")

print('Quit loop successfully!')
