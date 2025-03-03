# 创建一个集合set1，打印结果无序。
set1 = {"red", "blue", "green", "yellow"}
print(set1)
# 创 建一个集合set2，打印结果会去掉重复出现的元素。
set2 = {"a", "b", "c", "a"}
print(set2)
# 将元组转换为集合。
set3 = set(("Jane", "Judy"))
print(set3)
# 创建一个空集合。
set4 = ()
print(set4)
# 集合中元素为可变数据类型会报错。
set4 = {"red", "blue", ["green", "yellow"]}
print(set4)
