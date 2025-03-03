my_set = {"a", "b", "c", "d"}
x = "q"
# 将x增加到集合my_set中。
my_set.add(x)
print(my_set)
# 返回集合my_set的长度。
print(len(my_set))
# 将x从集合my_set中删除。
my_set.remove(x)
print(my_set)
# 从集合my_set中随机删除一个元素，并保存在变量y中。
y = my_set.pop()
print("删除的元素是：", y)
print("当前my_set为：", my_set)
# 判断元素“red”是否在集合my_set中。
if "b" in my_set:
    print("b in my_set")
else:
    print("b not in my_set")
# 为集合my_set创建一个副本temp_set。
temp_set = my_set.copy()
print(temp_set)
# 清空集合my_set。
my_set.clear()
print("集合已清空，结果为：", my_set)
