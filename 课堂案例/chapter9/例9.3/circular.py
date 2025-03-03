import math

Pi = math.pi


# 计算圆的周长
def girth(r):
    return round(2 * Pi * r, 2)


# 计算圆的面积
def area(r):
    return round(Pi * r * r, 2)


if __name__ == '__main__':
    print(girth(5), area(5))