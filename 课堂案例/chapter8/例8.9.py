class Animal():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self, food):
        print(self.name + "正在吃" + food)


class Dog(Animal):
    def eat(self, food, place):
        print(self.name + "正在吃" + food + "," + place)


dog1 = Dog("小花", 2, "白色")
print(dog1.name)
dog1.eat("面包", "它很高兴！")