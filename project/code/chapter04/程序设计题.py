import random
# 1.
# user = input('请注册账户')
# passwd = input('请输入密码')
# for i in range(1, 4):
#     user2 = input('请输入账户')
#     passwd2 = input('请输入密码')
#     if user2 == user and passwd2 == passwd:
#         print('登录成功')
#         break
#     else:
#         print('账号或密码输入错误，您还有%d次机会' %(3-i))
#         continue
# 参考答案
# count = 0 # 用于记录用户错误次数
# while count < 3:
#     user = input("请输入您的账号：")
#     pwd = input("请输入您的密码：")
#     if user == 'admin' and pwd == '123': # 进行账号密码比对
#         print('登录成功')
#         break
#     else:
#         print("用户名或密码错误")
#         count += 1 # 初始变量值自增 1
#         if count == 3: # 如果错误次数达到 3 次，则提示并退出
#             print("输入错误次数过多，请稍后再试")
#         else:
#             print(f"您还有{3 - count}次机会")  # 显示剩余次数

# 2.
# count = 0
# num_str = input('请分别输入成绩，用空格隔开：')
# grade = list(map(int, num_str.split()))
# for i in range(len(grade)):
#     if grade[i] < 60:
#         count +=1
# print(f'低于60分的同学的比例是：{(count/len(grade)) * 100}%')
# 参考答案
# count=0
# n=int(input("请输入学生人数："))
# for i in range(n):
#     score=int(input("请输入学生成绩："))
#     if score<60:
#         count+=1
#         continue
# print(count/n)

# 3.简易计算机
# 运算符：+ - * /
# num1 = int(input('请输入运算数：'))
# op = input('请输入运算符：')
# num2 = int(input('请输入运算数：'))
# sum = 0
# if op == '+':
#     sum = num1 + num2
#     print('结果是：', sum)
# elif op == '-':
#     sum = num1 - num2
#     print('结果是：', sum)
# elif op == '*':
#     sum = num1 * num2
#     print('结果是：', sum)
# elif op == '/':
#     sum = num1 // num2
#     print('结果是：', sum)
# 参考答案
# x=int(input("请输入第一个数："))
# y=int(input("请输入第二个数："))
# operator = input('请选择要执行的运算符：+、-、*、/' + '\n')
# if operator == "+":
#     print("计算结果为:", x + y)
# elif operator == '-':
#     print("计算结果为:", x - y)
# elif operator == '*':
#     print("计算结果为:", x * y)
# elif operator == '/':
#     if y == 0:
#         print('被除数不能为 0!')
#     else:
#         print("计算结果为:", x / y)

# 4.
# random_int = random.randint(1, 100)
# for i in range(1, 4):
#     num3 = int(input('请输入一个整数'))
#     if random_int == num3:
#         print('恭喜，我中了！')
#     elif random_int < num3:
#         print("赌大了")
#     elif random_int > num3:
#         print("赌小了")
#     print(f'还有{3 - i}次机会')
# 参考答案
# import random
# print("******** 猜数字小游戏 ********")
# print("猜数字游戏规则：输入一个 1-100 以内的数字,总共有3次机会！")
# random_num = random.randint(1, 100)  # 生成一个1-100的随机数
#
# for i in range(1,4):
#     number = input("请输入一个数字:")
#     if number.isdigit() is False:
#         print('请输入一个正确的数字')
#     elif int(number) < 0 or int(number) > 100:
#         print("请输入 1-100 范围的数字")
#     elif random_num == int(number):
#         print("恭喜你用了%d 次猜对了" % i)
#         break
#     elif random_num > int(number):
#         print("很遗憾，你猜小了")
#     else:
#         print("很遗憾，你猜大了")
#     if i == 3:
#         print("很遗憾，%d次机会已用尽，游戏结束,答案为%d" % (i, random_num))

# 砂金版
# random_int = random.randint(0, 2)
# print('这是一场豪赌：所有 或者 一无所有')
# while True:
#     num3 = int(input('赌一个0到1中的一个数:'))
#     if random_int == num3:
#         print('欢庆吧！琥珀王向你致敬！')
#         break
#     else:
#         print("老赌徒，满盘皆输！")
#         str = input('是否出千？y/n：')
#         if str == ('y'):
#             print('你赢了！结果并不重要，重要的是这根本不重要')
#         else:
#             print('我敬佩你这崇尚的道德水准，因此这是对你崇高道德的赞许 ')
#             num3 = int(input('你回到了起点，赌一个0到1中的一个数:'))
#             if random_int == num3:
#                 print('欢庆吧！琥珀王向你致敬！')
#                 break
#             else:
#                 print("老赌徒，满盘皆输！")

#5.输出:
#    *
#   ***
#  *****
# *******
# 化繁为简
# (1)先输出  *个数
# *          1
# ***        3          -->2i-1
# *****      5
# *******    7
# for i in range(1, 5):
#     for j in range(0, 2 * i - 1):
#         print('*', end='')
# print('\n')
# (2)         空格数
#    *         3
#   ***        2       --> 5-i-1
#  *****       1
# *******      0
# 在输出*之前输出空格
# for i in range(5):
#     # 在输出*之前输出空格
#     for k in range(5 - i - 1):
#         print(" ", end='')
#     for j in range(2 * i - 1):
#         print('*', end='')
#     print()
# 参考答案
# (1).
# for i in range(1, 7):
#     for j in range(1, (7-i)):
#         print(' ', end='')
#     for k in range(1, 2*i):
#         print('*', end='')
#     print()
# (2).
# h = int(input('输入：'))
# for i in range(1, h + 1):
#     print((h - i) * " ", end='')
#     print((i * 2 - 1) * "*")

# 6. 输出一个空心三角形
#    *
#   * *
#  *   *
# *******
# 借用5.
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

# 参考答案
# i = 1
# while i < 6:
#     j = 1
#     while j <= 5 - i:
#         print(' ', end='')
#         j += 1
#     j = 1
#     while j <= 2 * i - 1:
#         if j == 1 or i == 5 or j == 2 * i - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#         j += 1
#     print()
#     i += 1

# 7. 鸡兔同笼问题:
#        头      脚
# 鸡:    1       2
# 兔:    1       4
# sum = int(input('输入总个数:'))
# legs = int(input('输入脚有几只:'))
# rabbits = (legs - 2 * sum) // 2
# chickens = sum - rabbits
# if rabbits + chickens != sum or rabbits * 4 + chickens * 2 != sum:
#     print('输入有误')
# else:
#     print(f'兔子有:{rabbits}只,鸡有:{chickens}只')
# 参考答案
# for i in range(1,50):
#     for j in range(1,40):
#         if i+j==50 and 2*i+4*j==160:
#             print('鸡有%d只，兔有%d只' % (i,j))

# 8.输出四位整数中的所有回文数并统计个数
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

# 参考答案
# num = int(input("请输入一个四位数："))
# single = int(num / 1000)
# ten = int(num / 100 % 10)
# hundred = int(num / 10 % 10)
# ths = int(num % 10)
# num1 = ths * 1000 + hundred * 100 + ten * 10 + single
# if num == num1:
#      print(num,"是回文数")
# else:
#      print(num,"不是回文数")



