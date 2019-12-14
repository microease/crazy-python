# coding:utf-8
# File Name：     varargs
# Description :
# Author :       micro
# Date：          2019/12/13
def test(a, *books):
    print(books)
    for b in books:
        print(b)
    print(a)


test(4, "疯狂IOS讲义", "疯狂Android讲义")
