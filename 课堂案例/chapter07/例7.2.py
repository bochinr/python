def sumOddnumber():
    sum = 0
    for i in range(101):
        if i % 2 == 1:
            sum += i
    print("n以内所有的奇数和为：", sum)

sumOddnumber()  # 调用函数