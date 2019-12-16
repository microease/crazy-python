# coding:utf-8
# File Name：     print_object
# Description :
# Author :       micro
# Date：          2019/12/15
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


im = Item('鼠标', 19.8)
print(im)
print(im.__repr__())
