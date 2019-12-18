# coding:utf-8
# File Name：     PurePath_test
# Description :
# Author :       micro
# Date：          2019/12/17
from pathlib import *

pp = PurePath("setup.py")
print(type(pp))
pp = PurePath('crazyit','some/path','info')
print(pp)
pp = PurePath(Path('crazyit'),Path('info'))
print(pp)
pp = PurePosixPath()