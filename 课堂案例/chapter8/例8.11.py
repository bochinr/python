class Animal():
    def __init__(self, name):
        self.name = name

    def play(self, game):
        print(self.name + "正在玩" + game)


class Dog(Animal):
    def play(self, place, ball):
        print(self.name + "正在" + place + "在玩" + ball)


dog = Dog("小黄")
dog.play("花园里", "皮球")
