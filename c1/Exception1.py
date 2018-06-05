#!/usr/bin/env python
# -*-coding:utf-8-*-

try:  #  可能产生的异常代码需要写在try块中 ，try块在执行过程中一旦发生异常，则try块剩余的代码被终止执行
    result = 3/0
    print("This is never been called")
except:  #  except 块用于定义当某种异常发生时所要执行的代码
    print("Exception happened")
finally:  #  可选，无论try 块中是否有异常发生，其中的代码都会执行
    print("Process finished!")
