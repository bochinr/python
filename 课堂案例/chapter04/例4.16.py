str="Hello,Python"
j=1
while j<=3:
    for i in str:
        if i==',':
            break
        print(i,end='')
    print('')
    j=j+1