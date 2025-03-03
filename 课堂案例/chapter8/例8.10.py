# 定义沙发父类
class Sofa():
    color = "白色"

    def printA(self):
        print('这是' + Sofa.color + '沙发')


# 定义床父类
class Bed():
    color = "红色"

    def printB(self):
        print('这是' + Bed.color + '床')


# 定义一个子类，继承自沙发和床类
class Sofabed(Sofa, Bed):
    def printC(self):
        print('这是' + Sofa.color + '和' + Bed.color + '的沙发床')


sfd = Sofabed()
sfd.printA()
sfd.printB()
sfd.printC()
