def maxNum(a, b, *c):  # 求最大值
    max_value = a
    if max_value < b:
        max_value = b
    for n in c:
        if max_value < n:
            max_value = n
    return max_value
print(maxNum(1, 2, 5, 2, 4))
print(maxNum(1, 9, 11, 4, 25))