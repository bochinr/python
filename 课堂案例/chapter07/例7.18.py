def gcd(a, b):
    if (a % b == 0):  # 如果除数b等于0，不可以再继续进行辗转相除，此时的a就是最大公约数
        return b
    else:
        return gcd(b, a % b)

print(gcd(20, 15))
