# coding:utf-8
# File Name：     lambda_test
# Description :
# Author :       micro
# Date：          2019/12/14
def get_math_func(type):
    result = 1
    if type == 'square':
        return lambda n: n * n  # 平方
    elif type == 'cube':
        return lambda n: n * n * n  # 立方
    else:
        return lambda n: (1 + n) * n / 2