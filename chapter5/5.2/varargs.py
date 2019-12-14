# coding:utf-8
# File Name：     varargs
# Description :
# Author :       micro
# Date：          2019/12/14
def test(name,message):
    print("用户是:"+name)
    print("欢迎消息："+message)
my_list = ['孙悟空','欢迎来到疯狂软件']
test(*my_list)