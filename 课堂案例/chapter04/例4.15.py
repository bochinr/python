
for i in range(1,10):                   #外循环
    for j in range(1,i+1):        #内循环
        print("%d * %d = %d" % (j, i, i * j), end="  ")
    print()