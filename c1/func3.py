#!/usr/bin/env python
# -*-coding:utf-8-*-
# 变长函数
# 元组变长参数，适用于未知参数的数量不固定，但是在函数中使用这些参数时无须知道这些参数的名字的场合
# 在函数定义中，元组变长参数用星号 * 标记 message 是固定参数  tupleName 是变长参数


def show_message(message, *tupleName):
    for name in tupleName:
        print(message, ", ", name)


def check_book(**dictParam):
    if 'Price' in dictParam:
        price = int(dictParam['Price'])   #   'if dictParam.has_key('Price'):  python3 用in 取代了  has_key'
        if price > 100:
            print("*******I want buy this book!*******")
    print("The book information are as follow:")

    for key in dictParam.keys():
        print(key, ": ", dictParam[key])

    print("")


if __name__ == '__main__':
    show_message("Good morning", "Jack", "Evans", "Rose Hasa", 893, "Zion")
    check_book(author = 'James', Title = 'Economics Introduction')
    check_book(author = 'Linda', Title = 'Deepin in Python', Date='2015-5-1', Price = 302)
    check_book(Date = '2002-3-19', Title = 'Cooking book', Price = 20)
    check_book(author = 'Jinker Landy', Title = 'How to keep healthy')
    check_book(Category = 'Finance', Name = 'Enterprise Audit', Price = 105)
