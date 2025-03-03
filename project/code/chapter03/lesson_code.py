#p51
No = 114514
str1 = 'xiaoban teacher' #空格也算一个字符
age = 18
# print(str[0:5])
# print(str[5:0])  #不可取
# print(str[5:])
# print(str[:5])
# print(str[:])

# p52 format()方法的使用
# print("1""大家好，我是{}，学号是{},今年{}岁".format(str1, No, age))
# print("2""大家好，我是{0}，学号是{1}".format(str1, No))
# print("3""大家好，我是{1}，学号是{1}".format(str1, No))
# print("4""大家好，我是{1}，学号是{0}".format(str1, No))
# print("5"f'大家好，我是{str1}，学号是{No}')
# print("{:0<9d}".format(No)) #右补0，补充后的数字长度为9位
# print("{:1<9d}".format(No)) #右补1，补充后的数字长度为9位
# print("{:0>10d}".format(No))


# 字符串处理函数
# print(len(str1))
# print(str(str1))
# print(chr(97))
# print(ord('a'))
# a = 1
# print(type(a))
# print(type(str(a)))

# 字符串处理方法
# print("python".lower())
# print("python".upper())
# print('a b c c'.split())
# print('ab ca acd'.split('a'))
# print('ab ca acd'.count('a'))
# print('hello world'.replace(' ','I'))
# print('hello world'.replace('','I'))
# print('hello world'.replace('world','life'))
# print("i love elysia forever".center(1314,'*'))