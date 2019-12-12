# coding:utf-8
# File Name：     list_test
# Description :
# Author :       micro
# Date：          2019/12/12
a_tuple = "micorease", 24, "shenzhen"
a_list = list(a_tuple)
b_tuple = tuple(a_list)
print(a_tuple)
print(a_list)
print("++++++++++++++++++++++++++++++++++++++++++++++++++|")
print(dir(list))
b_list = [2, 30, "a", [5, 30], 30]
print(b_list.count(30))
print(b_list.index(2))
print("++++++++++++++++++++++++++++++++++++++++++++++++++|")

b_list.pop()
print(b_list)
print(b_list.pop())
print(b_list)
c_list = [1, 2, 3, 4, 5, 6, 7]
c_list.reverse()
print(c_list)
c_list.sort()
print(c_list)
