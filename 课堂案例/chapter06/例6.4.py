S="随风潜入夜，润物细无声。"
# 字符串正向索引。
print(S[5])
# 字符串反向引。
print(S[-1])
# 通过遍历循环可以索引字符串中的多个字符。
for i in range(0, 5):
    print(S[i], end=" ")
#索引index超过字符串的长度时，会报错。
print(S[13])