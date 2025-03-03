class Car:
    price = 460000  # 类成员

    def __init__(self, name, color):
        self.name = name
        self.color = color  # 实例成员


car1 = Car("奥迪", "red")  # 创建对象
print(car1.price, Car.price, car1.color)  # 访问类成员和实例成员并输出
Car.name = '宝马'  # 增加类成员
car1.wheelNum = 4  # 增加实例成员
print(car1.wheelNum, car1.name, Car.name)  # 访问类成员和实例成员并输出
