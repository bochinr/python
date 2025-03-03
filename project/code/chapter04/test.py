# 1.
# count = 1
# while True:
#     user = input("请输入账号")
#     passwd = input("请输入密码")
#     if user == "zhangsan" and passwd == "123":
#         print("登录成功")
#         break
#     elif count < 3:
#         print("密码错误，还剩%d次机会"%(3-count))
#     else:
#         print("次数过多")
#         break
#     count += 1

# 2.
# count = 0
# num = eval(input("输入学生人数"))
# for i in range(num):
#     score = eval(input("输入成绩"))
#     if score < 60:
#         count += 1
# print("占比为", count / num * 100, "%")

# 3.
# num1 = eval(input("输入第一个数"))
# num2 = eval(input("输入第二个数"))
# operator = eval(input("输入操作符"))
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     if num2 == 0:
#         print("除数不能为0")
#     else:
#         print(num1 / num2)

# 4.
# import random
# random_int = random.randint(1, 10)
# count = 0
# while count < 3:
#     num = eval(input("输入一个数字"))
#     if num == random_int:
#         print("bingo")
#         break
#     elif num > random_int:
#         print("big")
#     else:
#         print("small")
#     count += 1

# 5.
# for i in range(5):
#     # 在输出*之前输出空格
#     for k in range(5 - i - 1):
#         print(" ", end='')
#     for j in range(2 * i - 1):
#         print('*', end='')
#     print()

# 6.
# number_int = int(input('请输入层数:'))
# for i in range(number_int + 1): #左开右闭 number_int + 1 = 层数
#     # 在输出*之前输出空格
#     for k in range((number_int + 1) - i - 1):
#         print(" ", end='')
#     for j in range(2 * i - 1):
#         # 在输出*时进行判断:
#         # 如果是 该行的首位 或者 最后一位 或者 最后一行 则输出*
#         # 否则输出空格
#         if j == 0 or j == 2 * i -2 or i == number_int:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# 7.
# total = 50
# legs = 160
# rabbit = (legs - total * 2) / 2
# chiken = total - rabbit
# print("兔子有：", (legs - total * 2) / 2, "只")
# print("鸡子有：", chiken, "只")

# 8.
# sum = 0
# for循环输出所有四位整数
# for i in range(1000, 10000):
#     # 判断是否是回文数
#     thousand = i // 1000
#     hundred = i // 100 % 10
#     ten = i // 10 % 10
#     one = i % 10
#     if thousand == one and hundred == ten:
#         print(i)
#         sum += 1
# print(sum)
