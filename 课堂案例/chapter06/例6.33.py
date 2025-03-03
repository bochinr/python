person = {
    '张三': {
        '国籍': '中国',
        '民族': '壮',
        '出生日期': '1991年4月24日',
        '身高': '182cm',
    },
    '李四': {
        '国籍': '中国',
        '民族': '汉',
        '出生日期': '1976年4月12日',
        '身高': '176.5cm',
    }
}
for pname, pinfo in person.items():
    print('*********************************')
    print("姓名：", pname)
    for key, value in pinfo.items():
        print(key + ':' + value)
