#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

newlist = ['com.sec.location.nsflp2', 'com.sec.sve', 'com.sec.imsservice', 'com.android.com.wuba','com.android.a']
# for i in newlist:
#     if i.startswith("com.sec.") or i.startswith("com.samsung"):
#         newlist.remove(i)
# print("过滤系统应用进程",newlist,len(newlist))


# new_list = [newlist.remove(i) for i in newlist if  i.startswith("com.sec") == False]
# print("过滤系统应用进程",newlist,len(newlist))

"""
1、通过adb shell ps 获取到应用进程，处理成list
2、过滤掉以com.android或com.samsung开头的进程，notsyslist
3、过滤掉带冒号的子进程，如com.wuba:downloadapkservice
3、notsyslist和reallistA（埋点实际上报的进程）进行比对
"""
# os.system("adb shell ps |grep ""com.*"" |awk '{print $9,$10}' >e://adbps_test.txt")
with open("testtest.txt", 'r') as f:
    list= f.readlines()
    newlist=[]
    for i in list:
        # i.replace("\n","")
        newlist.append(i.rstrip())
    # print("step1、通过adb shell ps 获取到应用进程，处理成list",newlist,len(newlist))

# old_list = ['com.sec.location.nsflp2','com.sss.sve','com.sec.sve', 'com.sec.imsservice', 'com.android.com.wuba','com.android.com.wuba','com.android.a']
# new_list = old_list[:]
for i in range(len(newlist)-1,-1,-1):
    if newlist[i].startswith("com.android"):
        newlist.remove(newlist[i])
    # elif newlist[i].startswith("com.samsung"):
    #     newlist.remove(newlist[i])
# print("\n"+"step2、通过adb shell ps",newlist,len(newlist))
#过滤掉带冒号的子进程
for i in range(len(newlist)-1,-1,-1):
    if ":" in newlist[i]:
        newlist.remove(newlist[i])
# print("过滤掉带冒号的子进程",newlist,len(newlist))

#过滤samsung的进程
for i in range(len(newlist)-1,-1,-1):
    if newlist[i].startswith("com.samsung"):
        newlist.remove(newlist[i])
print("过滤samsung的进程",newlist,len(newlist))


#过滤com.sec的进程
for i in range(len(newlist)-1,-1,-1):
    if newlist[i].startswith("com.sec"):
        newlist.remove(newlist[i])
print("过滤com.sec的进程",newlist,len(newlist))
reallistA =["com.github.uiautomator","sogou.mobile.explorer","com.thinksky.itools","io.appium.settings","com.chailz.frescodemo","com.dx.agent2","com.wandoujia.phoenix2.usbproxy","com.shyz.toutiao","io.appium.uiautomator2.server","org.thisisafactory.simiasque","com.netease.nie.yosemite","com.tencent.mm","com.anjuke.android.app","com.samsung.android.app.watchmanager","com.huawei.hwid","com.netease.qa.emmagee","com.wuba","com.samsung.android.app.memo","cn.itools.tool.market","com.koushikdutta.vysor","com.mci.smagazine","com.screeclibinvoke","com.ndoo.pcassist","com.UCMobile","com.tencent.mobileqq","com.shuame.mobile","overdector.com.overdrawdector","flipboard.boxer.app","com.wandoujia.phoenix2","com.shuame.sprite","com.baidu.BaiduMap","com.samsung.android.onlinevideo","com.boco.alipay.activity","com.netease.open.pocoservice","com.sec.android.app.popupcalculator","com.qihoo.appstore","jackpal.androidterm","com.samsung.android.voc","com.mwr.dz","com.wuba.wchat","com.baidu.baidulocationdemo","com.iflytek.inputmethod","com.google.vr.inputcompanion","com.taobao.taobao","com.androidiii.appstore","net.oschina.app","com.eg.android.AlipayGphone"]
# reallistA = ["com.github.uiautomator","sogou.mobile.explorer","com.thinksky.itools","io.appium.settings","com.chailz.frescodemo","com.dx.agent2","com.wandoujia.phoenix2.usbproxy","com.shyz.toutiao","io.appium.uiautomator2.server","org.thisisafactory.simiasque","com.netease.nie.yosemite","com.tencent.mm","com.anjuke.android.app","com.samsung.android.app.watchmanager","com.huawei.hwid","com.netease.qa.emmagee","com.wuba","com.samsung.android.app.memo","cn.itools.tool.market","com.koushikdutta.vysor","com.mci.smagazine","com.screeclibinvoke","com.ndoo.pcassist","com.UCMobile","com.tencent.mobileqq","com.shuame.mobile","overdector.com.overdrawdector","flipboard.boxer.app","com.wandoujia.phoenix2","com.shuame.sprite","com.baidu.BaiduMap","com.samsung.android.onlinevideo","com.boco.alipay.activity","com.netease.open.pocoservice","com.sec.android.app.popupcalculator","com.qihoo.appstore","jackpal.androidterm","com.samsung.android.voc","com.mwr.dz","com.wuba.wchat","com.baidu.baidulocationdemo","com.iflytek.inputmethod","com.google.vr.inputcompanion","com.taobao.taobao","com.androidiii.appstore","net.oschina.app","com.eg.android.AlipayGphone"]
nulllist =[]
notinnewlist = []
bothlist = []
#去掉带三星的com.samsung的进程
for i in range(len(reallistA)-1,-1,-1):
    if reallistA[i].startswith("com.samsung"):
        reallistA.remove(reallistA[i])
print("reallistA过滤samsung的进程",reallistA,len(reallistA))
for i in reallistA:
    if i not in newlist :
        notinnewlist.append(i)
    else:
        bothlist.append(i)
print("埋点上报且adbps统计到的进程",bothlist,len(bothlist))
print("\n"+"未在adbshellps列表进程数量",notinnewlist,len(notinnewlist))
print("实际上报的进程数量",len(reallistA))
print("adb shell ps统计的进程数量,过滤系统应用进程",len(newlist))


notupdate = []
for i in newlist:
    if i not in reallistA:
        notupdate.append(i)
print("埋点未上报进程",notupdate,len(notupdate))


#####处理实际上报的埋点数据
with open("real.txt", 'r') as f:
    list= f.readlines()
    print("(((((((((((((((")
    print(type(list),list[0])
    newlist = list[0].split("|")
    print("(***********")
    print(type(newlist),newlist)
    newlist=[]
    for i in list:
        newlist = i.split("|");

        # aa=aa.replace("|","\',\'")
        # i.replace("\n","")
        print("ssfsfsd",newlist,len(newlist),type(newlist))
        # newlist.append(aa.rstrip())
# print("newlistnewlist",newlist,len(newlist))
for i in range(len(newlist)-1,-1,-1):
    if newlist[i].startswith("com.coloros"):
        newlist.remove(newlist[i])
print("\n oppo reno 过滤com.coloros",newlist,len(newlist))