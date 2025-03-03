# 计算矩形周长
def girth(width, height):
    return (width + height) * 2


# 计算矩形面积
def area(width, height):
    return width * height

if __name__ == '__main__':
    print(girth(5, 5), area(5, 5))