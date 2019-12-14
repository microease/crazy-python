# coding:utf-8
# File Name：     varargs
# Description :
# Author :       micro
<<<<<<< HEAD
# Date：          2019/12/13
def test(a, *books):
    print(books)
    for b in books:
        print(b)
    print(a)


test(4, "疯狂IOS讲义", "疯狂Android讲义")
=======
# Date：          2019/12/14
def test(name,message):
    print("用户是:"+name)
    print("欢迎消息："+message)
my_list = ['孙悟空','欢迎来到疯狂软件']
test(*my_list)
>>>>>>> c9d62f7f264cfdff21d556a8a6789fab79173d9c
