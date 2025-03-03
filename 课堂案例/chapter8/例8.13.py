# 人开枪射击子弹
# 创建人类
class Person():
    def __init__(self, gun):
        self.gun = gun

    def fire(self):
        self.gun.shoot()

    def fill_bullet_box(self, count):
        self.gun.bulletbox.bulletcount = count
        print("你装上了%d颗子弹，又可以射击了" % count)


# 创建枪类
class Gun():
    def __init__(self, bulletbox):
        self.bulletbox = bulletbox

    def shoot(self):
        if self.bulletbox.bulletcount == 0:
            print("没子弹了，赶紧装弹吧...")
        else:
            self.bulletbox.bulletcount -= 1
            print("砰地开了一枪，你还剩%d颗子弹" % self.bulletbox.bulletcount)


# 创建弹匣类
class BulletBox():
    def __init__(self, bulletcount):
        self.bulletcount = bulletcount

if __name__ == '__main__':
    bulletbox = BulletBox(2)  # 实例化弹匣，并装入子弹
    gun = Gun(bulletbox)  # 实例化枪，并装入弹匣
    per1 = Person(gun)  # 实例化人，并给一把枪
    per1.fire()  # 开枪
    per1.fire()
    per1.fire()
    per1.fill_bullet_box(2)  # 装弹
    per1.fire()
