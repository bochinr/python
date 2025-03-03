class Car:
    def col(self, color):  # 定义赋值颜色方法
        self.col = color  # 赋值

    def show(self):  # 定义显示颜色方法
        print('汽车的颜色是：%s。' % self.col)  # 输出颜色

car1 = Car()  # 创建对象car1
car1.col('红色')  # 调用方法
car2 = Car()  # 创建对象car2
car2.col('白色')  # 调用方法
car1.show()  # 调用方法
car2.show()  # 调用方法
