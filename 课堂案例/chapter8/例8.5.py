class Cat(object):
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.hobby = "运动"

    def eat(self, food):
        print("一只" + self.color + "的" + self.name + "正在吃" + food)
        print(self.name + "喜欢" + self.hobby)

cat1 = Cat("咪咪", 2, "白色")
cat2 = Cat("嘟嘟", 1, "灰色")
cat3 = Cat("哆啦", 2, "黄色")
cat1.eat("鱼")
cat2.eat("面包")
cat3.eat("鸡肉")
