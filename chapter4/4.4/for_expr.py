# coding:utf-8
# File Name：     for_expr
# Description :
# Author :       micro
# Date：          2019/12/12
a_range = range(10)
a_list = [x * x for x in a_range if x % 2 == 0]
print(a_list)
