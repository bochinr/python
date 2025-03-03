from math import *

height = int(input("请输入等腰三角形的高："))
for i in range(1, height + 1):
    print((height - i) * " ", end='')
    print((i * 2 - 1) * "*")
