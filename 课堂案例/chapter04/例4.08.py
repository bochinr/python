print("欢迎进入快递计费系统！")
weight = float(input("请输入快递重量："))
print('编号 01：偏远地区 编号 02：港澳台地区 编号 03：其他地区')
num = input("请输入地区编号：")
if weight <= 3:
    if num == '01':
        print('快递费为 15 元')
    elif num == '02':
        print('快递费 16 元')
    elif num == '03':
        print('快递费 12 元')
else:
    weight_remain = weight - 3
    if num  == '01':
        many = weight_remain * 5 + 15
        print('快递费为%.1f 元' % many)
    elif num== '02':
        many = weight_remain * 6 + 16
        print('快递费为%.1f 元' % many)
    elif num == '03':
        many = weight_remain * 4 + 142
        print('快递费为%.1f 元' % many)