def argcount(args):
    count = 0
    for i in args:
        count += 1
    return count

strs = input("请输入要统计长度的字符串：")
acount = argcount(strs)
print(acount)