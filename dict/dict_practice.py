#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhongyaqi'

import json

tep_dict ={1: 2, 2: 4}
tep_json ='{1: 2, 2: 4}'

print(type(tep_dict),type(tep_json))

# Python3 字典类型转换为 JSON 对象
info = {
    'name': 'xx',
    'sex': '女',
    'age': '18',
    'E-mail': 'zsfs@163.com'
}

json_info = json.dumps(info)  # 字典转JSON
print('info数据类型：', type(info))
print(json_info)
print('json_info数据类型：', type(json_info))

info1 = json.loads(json_info)   #str转dict
print(info1,'info1数据类型：',type(info1))
