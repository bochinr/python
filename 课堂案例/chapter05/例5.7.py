filename=input("请输入文本文件名：")
try:
    f=open(filename,"r")
    try:
        n=int(f.read())
        s=1
        for i in range(1,n+1):
            s=s*i
        print("数据{}的阶乘为{}".format(n,s))
    except:
        print("文本内数据不为整数，数据不匹配！")
    finally:
        f.close()
except:
    print("文本文件不存在！")