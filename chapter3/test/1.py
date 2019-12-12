# coding:utf-8
# File Name：     1
# Description :
# Author :       micro
# Date：          2019/12/12
# 需求：提示用户输入N个字符串，将他们封装成元组，再计算并输入该元组乘以3的结果，再计算并输出该元组加上('author','huyankai')。
str_1 = input("请输入N个字符串,以空格分开:")
tuple_1 = tuple(str_1.split(" "))
print(tuple_1*3+('author','huyankai'))