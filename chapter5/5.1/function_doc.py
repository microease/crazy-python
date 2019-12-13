# coding:utf-8
# File Name：     function_doc
# Description :
# Author :       micro
# Date：          2019/12/13
def my_max(x,y):
    """
    获取两个数值中比较大的数
    """
    z = x if x >y else y
    return z
help(my_max)
print(my_max.__doc__)