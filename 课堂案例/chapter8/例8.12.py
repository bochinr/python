# 创建父类Man
class Man():
    def eat(self):
        print("时间到了，开饭喽!")


# 创建子类Chinese，并重写父类的eat()方法
class Chinese(Man):
    def eat(self):
        print("请拿上你的碗筷-开饭了")


# 创建子类Japan，并重写父类的eat()方法
class Japan(Man):
    def eat(self):
        print("请洗干净你的手-开饭了")


# 创建子类American，并重写父类的eat()方法
class American(Man):
    def eat(self):
        print("请拿上你的刀叉-开饭了")


# 主函数
def main(m):
    if isinstance(m, Man):  # 判断传入的m和MAN的类型是否相同
        m.eat()  # 此处便是多态，根据对象不同调用不同的方法
    else:
        print("不能吃饭")


if __name__ == '__main__':
    while True:
        nat = input("请输入你的国籍(q退出)：")
        if nat == "q":
            break
        elif nat == "Chinese":
            main(Chinese())
        elif nat == "Japan":
            main(Japan())
        elif nat == "American":
            main(American())
        else:
            main("other")
