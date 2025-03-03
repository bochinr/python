price = [399, 4369, 539, 288, 109, 749, 235, 190, 99, 1000]
temp = []
max_price = int(input("请输入最大价格:"))
min_price = int(input("请输入最小价格:"))
for i in price:
    if min_price <= i <= max_price:
        temp.append(i)
print("1.价格降序排序")
print("2.价格升序排序")
choice_num = int(input("请选择排序方式:"))
if choice_num == 1:
    temp.sort(reverse=True)
else:
    temp.sort()
print(temp)
