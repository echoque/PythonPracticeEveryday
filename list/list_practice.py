#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhongyaqi'

from collections import  Counter


"""1、从一个ｌｉｓｔ中找出奇数和偶数，奇数排在偶数前面"""
def reverse(tem_list):
    # tem_list = [1,2,2,4,7,6,22,2]
    even = list(filter(lambda i:i%2 == 0,tem_list))
    odd =list(filter (lambda i:i%2 != 0,tem_list))
    ##方法一，使用符号+号拼接
    # print(even+odd)    #偶数在前，奇数在后
    # print(odd+even)     #奇数在前，偶数在后
    ##方法二,使用extend函数
    odd.extend(even)
    print(odd)

"""2、list获取重复的元素及重复次数"""
def repeat(test_list):
        b = dict(Counter(test_list))
        print ({key:value for key,value in b.items()if value > 1})
"""3、list 去重且不新建list"""
def repeat2(tem_list):
    b = dict(Counter(tem_list))
    print(b,list(b.keys()))
"""list 去重且不新建list 使用set"""
def repeat3(tem_list):
    print(list(set(tem_list)))
if __name__ == '__main__':
    tem_list = [1,1,2,7,2,2,2]
    repeat(tem_list)
    repeat2(tem_list)
    repeat3(tem_list)
