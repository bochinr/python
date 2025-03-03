ls=["C语言","C++","Java","Python"]
s = ",".join(ls)
f=open("TIOBE.csv", 'w')
f.write(s)
f.close()


