# coding:utf-8
# File Name：     list_append
# Description :
# Author :       micro
# Date：          2019/12/12
a_list = ["microease", 24, "wuhan", "shenzhen"]
a_list.append("jianli")
print(a_list)
a_list.append([1,1,2,3])
print(a_list)
a_list.extend([1,2,3,4])
print(a_list)
print("++++++++++++++++++++++++++++++++++++++++++++++++++|")
c_list = list(range(1,10))
print(c_list)
c_list.insert(2,666666666666666666666666)
print(c_list)
del c_list[2]
print(c_list)
c_list.remove(3)
print(c_list)
c_list[-1] = 10
print(c_list)