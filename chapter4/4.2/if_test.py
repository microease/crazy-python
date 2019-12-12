# coding:utf-8
# File Name：     if_test
# Description :
# Author :       micro
# Date：          2019/12/12
a_age = input("请输入您的年龄")
age = int(a_age)
assert age > 20
if age > 20:
    print("您的年龄已经大于20岁了，要承担责任了。")
