n=int(input("请输入一个整数："))
if n%3==0 and n%5==0:
    print(n,"能同时被3和5整除")
else:
    print(n,"不能同时被3和5整除")