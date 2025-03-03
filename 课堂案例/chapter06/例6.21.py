ls = [12, "34", 56, "12", 34, "56", 'ab', '12a']
sum = 0
for item in ls:
    if type(item) == type(123):
        sum += item
print("列表ls中各整数元素的和为：", sum)

"""
ls =[12, "34", 56, "12", 34, "56", 'ab', '12a']
sum = 0
for i in range(len(ls)):
    if type(ls[i]) == type(1):
        sum += ls[i]
print("列表ls中各整数元素的和为：", sum)
"""