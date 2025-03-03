try:
    pi = 3.14
    n = int(input("请输入一个整数的圆的半径："))
    print("该圆的面积为：", pi * n ** 2)
except:
    print("输入错误，圆的半径要求为整数！")
