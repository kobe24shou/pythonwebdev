#!/usr/bin/env python
# -*-coding:utf-8-*-


class MyClass(object):   #  类名MyClass

    message = "hello ,developer"   # 类中定义一个成员变量 message，并对其赋了初始值

    def show(self):  # 类中 定义了成员函数 show(self)  类中的成员函数必须要带参数self
        print(self.message)
