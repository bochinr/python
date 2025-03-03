l = [100, 0x100, 0b100, 0o100]
# 在列表l末尾添加元素100.01。
l.append(100.01)
print(l)
# 在列表第0项添加元素"Python"。
l.insert(0, "Python")
print(l)
# 在列表末尾增加列表，新增列表元素作为原列表的元素。
l.extend(["计算机", "技术"])
print(l)
# 将列表第0项取出赋值给变量a，并在列表中删除该项元素。
a = l.pop(0)
print(a)
print(l)
# 将列表中第一个出现的元素“技术”删除。
l.remove("技术")
print(l)
# 列表反转。
l.reverse()
print(l)
# 用列表l复制一个新列表ls。
ls = l.copy()
print(ls)
# 清空列表。
ls.clear()
print(ls)
# 列表正序排序。
ls1 = [7, 1, 10, 0, 3, 8, 9, 6, 5, 4, 2]
ls1.sort()
print(ls1)
# 列表反序排序。
ls1.sort(reverse=True)
print(ls1)
# 列表中元素类型不同，排序会报错。
ls2 = ["java", "c++", 12, 34.56]
print(ls2.sort())
