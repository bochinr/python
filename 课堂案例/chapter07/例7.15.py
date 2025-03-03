result = 0  # 这是一个全局变量

def multiply(num1, num2):  # par1和par2为局部变量
    result = num1 * num2  # total在这里是局部变量.
    print("函数内是局部变量 : ", result)
    return result

multiply(10, 10)  # 调用sum函数
print("函数外是全局变量 : ", result)
