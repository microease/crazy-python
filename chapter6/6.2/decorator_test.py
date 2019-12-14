# coding:utf-8
# File Name：     decorator_test
# Description :
# Author :       micro
# Date：          2019/12/14
def funA(fn):
    print("A")
    fn()
    return "hello"


@funA
def funB():
    print("B")


print(funB)
