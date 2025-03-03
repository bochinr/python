f=open("F:\Python\Code\chapter10\data.txt","r", encoding="utf-8")
s=f.readline()
print(type(s))
while s:
    print(s)
    s = f.readline()
f.close()


