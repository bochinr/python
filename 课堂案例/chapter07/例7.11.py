def result(x, y):
    n = x % y
    if n == 0:
        print("这两个数商的余数为0！")
    else:
        if x % n == 0 and y % n == 0:
            print("这两个数商的余数能整除这两个数。")
        else:
            print("这两个数商的余数不能整除这两个数。")
r=result(5, 3)
r1=result(10, 4)

print(r)
print(type(r))
print(type(r1))