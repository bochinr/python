t1 = ("hello", 1000, "计算机技术")
t2 = ("Python",)
# 判断字符串是否是元组t1的元素。
print("Python" in t1)
# 元组t1和元组t2连接，生成新的元组t。
t = t2 + t1
print(t)
# 将元组t2复制2次。
print(t2 * 2)
# 返回元组t的长度。
print(len(t))
# 删除元组t。
del t
print(t)
