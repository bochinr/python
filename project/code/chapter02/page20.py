# #p19
# #输出1 - 100自然数的和
# sum = 0
# i = 1
# while i <= 100:
#     sum +=i
#     i += 1
# print(sum)
#
# #p20
# '''
# 请打印你的学号！
# 打印你的名字！
# '''
# print("2210180232")
# print("李胜志")
#
# print("{}和{}是同学".format(\
#     "老班",\
#     "小班"\
#     ))
#
# s=("小班"
#    "和老班"
#    "是朋友")
# print(s)
#
#
# #p27
# pi = 3.141592648
# r = 2
# s = pi * r ** 2
# print(s)

# #p28
# '''求一个梯形的面积'''
# a = 3
# b = 6
# h = 9
# s = 1/2 * h * (a + b)
# print("上底为",a,"下底为",b,"高为",h,"面积为",s)

'''
p29
赋值运算符的使用
'''
a = 4
b = 6
a *= b + a  #等价于a = a * ( b + a )
print(a)

# x = 456
# y = x % 10 * 100 + x // 10 % 10 * 10 + x // 100
# print(y)

# #p30
# import time
# time1 = time.gmtime()
# time2 = time.gmtime()
# timestamp = time.mktime(time2)
# print(time1)
# print(timestamp)