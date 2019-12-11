# coding=utf-8
b1 = bytes()
print(b1)
b2 = b'hello'
print(b2)
b3 = bytes('我爱Python', encoding='utf-8')
print(b3)
st3 = b3.decode("utf-8")
print(st3)
