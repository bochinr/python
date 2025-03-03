a = 2  # 全局变量
b = 3  # 全局变量


def my_func(x, y):
    global a  # 全局变量，与前面的全局变量a指向相同的对象a=2
    global m
    print('函数内 a=', a)
    b = 3.3  # 局部变量，与前面的全局变量b指向不同的对象
    print('函数内 b=', b)
    m = x * y
    print(m)


print('函数调用前 a=', a)
print('函数调用前 b=', b)
my_func(2, 5)
print('函数调用后 a=', a)
print('函数调用后 b=', b)
print(m)
