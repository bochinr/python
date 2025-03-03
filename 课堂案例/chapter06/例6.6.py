S1 = "hello "
S2 = "Python"
# 字符串S1和字符串S2连接，生成新的字符串S。
S = S1 + S2
print(S)
# 将字符串S1复制3次。
print(S2 * 3)
# 返回字符串S的长度。
print(len(S))
# 返回字符串S2中的最小值。
print(min(S2))
# 返回字符串S2中的最大值。
print(max(S2))
# 返回字符“o”在字符串S中第一次出现的位置。
print(S.index("o"))
# 返回字符“o”在字符串S中从下标6到11（不包含第11个）第一次出现的位置。
print(S.index("o", 6, 11))
# 返回字符“o”在字符串S中出现的次数。
print(S.count("o"))
