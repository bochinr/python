
# a = "abcdefghijklmnopqrstuvwxyz"
# print(a[:2])
# print(a[0:-1])
# print(a[-1:])
# print(a[-1:0])
# print(a[-1:2])
# print(a in a)
# print( a not in a )
# print(min(a))
# print(max(a))
# print( a.index("j", 2, 25))
# print(a.index("j", 2))
# print(a.index("j", 2))
# print(a.index("j", 2, 25))
# print(a.count('a'))

# lst = [1, 2, 3, 2, 1]
# print(len(lst))
#
# for i in range(len(lst)):
#     if lst[i] == 3:      #i =  1 & 3
#         print(lst.index(i), "yes")
# b = 'abc'
# b = b'abc'    #这都行
# print(b.index(b'a'))

# 使用内置对象方法slice对复杂的数据进行切片操作  slice（start stop step)
# s = 'kiana'
# s1 = slice(0, len(s), 1)
# print('1', s1)
# print(s[s1])
# print(s[slice(0, 2)])
#
# print(s1.stop)
# print(s1.start)
# print(s1.step)
# indices(len) 根据len自动匹配stop的值
# print(s1.indices(2))
# print('2', s1)
# s1 = s1.indices(1)
#
# # print('3', s1)
# s2 = "tech otakus sava the world!"
# print(s2[slice(0, len(s2))])
# print(slice(0, len(s2)).indices(3))
# print(s2[slice(0, len(s2), 1).indices(3)])

# p109
# for i in range(4):
#     print(i * "*")
# s1 = 'abc'
# print(s1 * 3)

# h = int(input('输入：'))
# for i in range(1, h + 1):
#     print((h - i) * " ", end='')
#     print((i * 2 - 1) * "*")

# 倒立金字塔
# h = int(input('输入：'))
# for i in range(1, h + 1):
#     print((i - 1) * " ", end='')
#     print(((2 * h) - (2 * i - 1)) * "*")


