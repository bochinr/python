# 判断用户传入的对象（字符串、列表、元组）长度是否大于5
def func(p):
    leng = len(p)
    print(leng)
    if leng > 5:
        print('Yes,the length higher than 5')
    else:
        print('NO')
