s = 'abcdef'
s1 = slice(1, len(s), 2)
print(s1)  # slice(1，6，2)
print(s[s1])  # 'bdf'
print(s1.start, s1.stop, s1.step)  # (1，6，2)
print(s1.indices(100))  # (1，6，2)
print(s1.indices(4))  # 根据长度，自动调整stop的值：(1，4，2)
