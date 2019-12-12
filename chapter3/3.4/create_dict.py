# coding:utf-8
# File Name：     create_dict
# Description :
# Author :       micro
# Date：          2019/12/12
scores = {'语文': 89, '数学': 92, '英语': 93}
print(scores)
print(scores['语文'])
scores['物理'] = 120
print(scores)
# scores.clear()
print(scores.get("语文"))
scores.pop("物理")
print(scores)