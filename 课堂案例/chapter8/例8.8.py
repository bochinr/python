class Person():
    def __init__(self, name, money):
        self.name = name
        self.__money = money    # 定义私有变量__meoney

    def __show(self):  # 定义私有方法__show( )
        print(self.name + "有" + str(self.__money) + "块钱")

per1 = Person("张三", 10)
# per1.__show()         # 报错，外部不可以访问内部私有方法
# print(per1.__money)   # 报错，外部不可以访问内部私有变量
"""
Python目前的私有机制其实是伪私有，实际上，在外部可以通过“_类名__属性”访问私有变量和方法。例如：
print(per._Person__money)	   #通过类名访问私有变量
per. _Person__show( )	       #通过类名调用私有方法
"""
