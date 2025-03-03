class Car:
    price = 460000  # 类成员

    def __init__(self):
        self.price = 200000  # 实例成员


car1 = Car()  # 创建对象
print("实例属性price:" + str(car1.price), "类属性price:" + str(Car.price))
