# coding:utf-8
# File Name：     locals_test
# Description :
# Author :       micro
# Date：          2019/12/14
def test():
    age = 20
    print(age)
    print(locals())
    print(locals()['age'])
    locals()['age']
    print('xxx',age)
    globals()['x'] = 19
x = 5
y = 20
test()
print(globals())
