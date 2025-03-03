dic = {"Jaimin": ["男", 185, 25],
       "Lucy": ["女", 167, 22],
       "James": ["男", 198, 37],
       "Nancy": ["女", 160, 24],
       "Alice": ["女", 160]}
# 输出字典dic的长度。
print(len(dic))
# 输出字典dic中键的最小值。
print(min(dic))
# 返回字典dic中键的最大值。
print(max(dic))
# 以字典键升序排序。
print(sorted(dic))
# 以字典键降序排序。
print(sorted(dic, reverse=True))
# 以字典值升序排序。
print(sorted(dic.values()))
# 以字典值降序排序。
print(sorted(dic.values(), reverse=True))
# dickeys()返回字典中的所有键信息，返回结果是内部数据类型dict_keys，若要更好的使用返回结果，需将其转换为列表类型，例如：
print(dic.keys())
print(type(dic.keys()))
print(list(dic.keys()))
# dicvalues()返回字典中的所有值信息，返回结果是内部数据类型dict_values，若要更好的使用返回结果，需将其转换为列表类型，例如：
print(dic.values())
print(list(dic.values()))
# dicitems()以元组形式返回字典中的键值对，返回结果是内部数据类型  	dict_items，若要更好的使用返回结果，可以将其转换为列表类型。
print(dic.items())
print(list(dic.items()))
# 键在字典中存在，则返回对应的值。
print(dic.get("Jaimin"))
# 键在字典中不存在，则返回默认值。
print(dic.get("Ali", "该姓名在字典中不存在"))
# 键在字典中存在，则取出对应的值，放入变量x中，同时在字典中删除键值对。
x = dic.pop("Lucy")
print(x)
print(dic)
# 随机从字典中取出一个键值对，以元组(key,value)形式返回，同时在字典中删除键值对。
dic.popitem()
print(dic)
# 向字典中增加一个键值对update。
dic.update({"Tommy": ["男", 172, 25]})
print(dic)
# 判断键是否在字典d的键中。
if "Nancy" in dic.keys():
    print("Yes!!!")
# 判断值是否在字典d的值中。
if "address" in dic.values():
    print(True)
else:
    print(False)
