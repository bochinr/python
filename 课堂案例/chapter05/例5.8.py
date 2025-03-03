try:
    n1 = float(input("请输入被除数n1："))
    n2 = float(input("请输入除数n2："))
    n = n1 / n2
    print("{}/{}={}".format(n1, n2, n))
except ZeroDivisionError:
    print("除数n2不能为0！")
except ValueError:
    print("被除数n1和除数n2应为数值类型的数据！")
