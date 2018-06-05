#!/usr/bin/env python
# -*-coding:utf-8-*-


def sum(x, y):
    return x + y


def total(x, y, z):
    sum_of_two = sum(x, y)
    sum_of_three = sum(sum_of_two, z)
    return sum_of_two, sum_of_three

#   定义了没有参数和返回值 的 main()函数


def main():
    print("return of sum:", sum(4, 6))
    x, y = total(1, 7, 10)
    print("return of total:", x, ",", y)



if __name__ == '__main__':
    main()