a = int(input('请输入第一个数字：'))
b = int(input('请输入第二个数字：'))
c = int(input('请输入第三个数字：'))
if a > b:
    if a>c:
        max = a
    else:
        max =c
else:
    if b>c:
        max = b
    else:
        max =c
print('输出最大值是：',max)