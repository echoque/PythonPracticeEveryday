#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhongyaqi'

#1、string和list互换类型
tep_str = "erewrwew"
print(list(tep_str),type(list(tep_str)))

list = [1,66,"tsr",2]
print(str(list),type(str(list)))

#2、字符串shuidi 变成idiuhs
def reverse(str):
    tem_str1 = str[:: -1]
    print(tem_str1)


def function_args(x, y, *args):
    print(x, y, args)
function_args(1, 2, 3, 4, 5)

def function_kwargs(**kwargs):
    print(kwargs)
function_kwargs(a=1, b=2, c=3)

tuple1 =(1)
tuple2 = (1,)
tuple3 = (1,1,1,1,2)
list1 = [1,2,3,1,1]
print(tuple1,"\n")
print(tuple2,"\n")
print(tuple3,"\n")
set1 = (1,3,2,1)
print("set",set(list1))
if __name__ == '__main__':
    __author__ = 'zhongyaqi'
    # reverse(__author__ )

