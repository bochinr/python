import json
import time


# 公共函数-写文件
def write_file(d, file):
    with open(file, 'w', encoding="utf-8") as fw:
        json.dump(d, fw, indent=2, ensure_ascii=False)  # 把字典写到文件中


# 公共函数-读文件
def read_file(file):
    dict = {}
    with open(file, 'r', encoding="utf-8") as fw:
        # fw.seek(0)      #判断之前要指定文件指针
        if len(fw.read()) > 0:
            fw.seek(0)  # 判断之后指针在最后面，所以再次指定位置，方面load
            dict = json.load(fw)
        return dict  # 返回一个字典或者是一个空字典


# 1、判断一个数为float或者正数
def check_float(num):
    num = str(num)
    if num.isdigit():
        return True
    elif num.count('.') == 1:
        left, right = num.split('.')
        if left.isdigit() and right.isdigit():
            return True
    return False


# 2、判断一个数为正数
def check_int(num):
    num = str(num)
    if num.isdigit():
        return True
    return False


# 3、添加商品：1、读取文件内容 2、判断商品名称是否存在 3、存在时数量+1 ，其他不变  4、不存在重新添加
# 文件保存
def add_product(file):
    product_name, product_count, product_price = panduan_product('add')
    dict_file = read_file(file)  # 读取文件中的数据进行判断
    # print(dict_file)
    if product_name in dict_file.keys():
        old_count = int(dict_file[product_name]['count'])
        dict_file[product_name]['count'] = old_count + int(product_count)
    else:
        dict_str = {product_name: {'count': product_count, 'price': product_price}}
        dict_file.update(dict_str)
    write_file(dict_file, file)
    print("添加成功")
    time.sleep(2)


# 4、判断商品是否符合要求，并返回正确的商品名称、要修改的商品名称、商品数量、商品价格
def panduan_product(flag):
    product_name = ""
    update__name = ""
    product_count = ""
    product_price = ""
    if flag == 'update':
        product_name = input('请输入原商品名称：').strip()
        update__name = input('请输入要修改的名称：').strip()
        product_count = input('请输入要修改的商品数量：').strip()
        product_price = input('请输入要修改的商品价格：').strip()
    elif flag == 'add':
        product_name = input('请输入商品名称：').strip()
        product_count = input('请输入商品数量：').strip()
        product_price = input('请输入商品价格：').strip()
    flag_count = check_int(product_count)
    flag_price = check_float(product_price)
    while not flag_count:
        product_count = input('请重新输入商品数量，数量只能是大于0的整数：').strip()
        flag_count = check_int(product_count)
    while not flag_price:
        product_price = input('请重新输入商品价格，价格可以是小数、整数，并且要大于0：').strip()
        flag_price = check_float(product_price)
    if flag == 'update':
        return product_name, update__name, product_count, product_price
    elif flag == 'add':
        return product_name, product_count, product_price


# 5、删除的商品的时候输入商品名称，商品不存在，要提示
def update_product(file):
    product_name, update_name, product_count, product_price = panduan_product('update')
    dict_file = read_file(file)  # 读取文件中的数据进行判断
    # print(dict_file)
    if product_name in dict_file.keys():
        dict_file[product_name]['count'] = product_count
        dict_file[product_name]['price'] = product_price
        dict_file[update_name] = dict_file.pop(product_name)  # 修改key的方法是pop原来的key返回key的value赋值给新key
        write_file(dict_file, file)
        print("修改成功")
    else:
        print("未找到该商品")


# 6、删除的商品的时候输入商品名称，商品不存在，要提示
def del_product(file):
    product_name = input('请输入删除商品名称：').strip()
    dict_file = read_file(file)  # 读取文件中的数据进行判断
    if product_name in dict_file.keys():
        dict_file.pop(product_name)
        write_file(dict_file, file)
        print("删除成功")
    else:
        print("未找到该商品")


# 7、查看商品，输入商品名称，查询到商品的信息
def show_product(file):
    product_name = input('请输入要查看的商品名称：').strip()
    dict_file = read_file(file)  # 读取文件中的数据进行判断
    if product_name in dict_file.keys():
        price = dict_file[product_name]['price']
        count = dict_file[product_name]['count']
        print("商品名称:%s\n数量:%s\n价格:%s元\n" % (product_name, count, price))
    else:
        print("未找到该商品")


if __name__ == '__main__':
    while True:
        choice = (input('====================\n'
                    '佳佳超市商品管理系统1.0\n'
                        '1.添加商品\n'
                        '2.删除商品\n'
                        '3.修改商品信息\n'
                        '4.查看商品\n'
                        '5.退出\n'
                        '====================\n'
                        '请输入你的选择：\n')).strip()
        if choice.isdigit() and int(choice) == 1:
            add_product('product.json')
        elif choice.isdigit() and int(choice) == 2:
            del_product('product.json')
        elif choice.isdigit() and int(choice) == 3:
            update_product('product.json')
        elif choice.isdigit() and int(choice) == 4:
            show_product('product.json')
        elif choice.isdigit() and int(choice) == 5:
            quit('程序退出')
        else:
            print("输入的数字不合法，请重来!!")
