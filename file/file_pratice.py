#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhongyaqi'

file = open("..//testdata//a.log","r")
new_list = []
num_list = []
# print(type(file))  #<class '_io.TextIOWrapper'>
for num,value in enumerate(file):
    # print(type(enumerate(file)))  #<class 'enumerate'>
    # print(list(enumerate(file)))  #[(0, '[warning]poiuoytrr2\n'), (1, '[warning]poiuoytrr3\n'), (2, '[warning]poiuoytrr4\n'), (3, '[error]huiiuiopp5\n'), (4, '[error]huiiuiopp6')]
    print(num,value)
    if value.startswith("[error]"):
        new_list.append(value.strip())
        num_list.append(num+1)
        # print(value,num+1)
print(new_list)
print("共出现%d次，"%len(new_list),"错误日志分别为",new_list,",出现行号：",num_list)
