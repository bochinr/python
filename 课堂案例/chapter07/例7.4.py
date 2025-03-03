def demo(obj):  # obj为形参
    obj += obj
    print("形参值为：", obj)
print("-------值传递-----")
a = "C语言中文网"  # a为实参
print("a的值为：", a)
demo(a)
print("实参值为：", a)
print("-----引用传递-----")
b = [1, 2, 3]
print("b的值为：", b)
demo(b)
print("实参值为：", b)
