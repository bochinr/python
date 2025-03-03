print(8>=8) #输出True
print(8==6) #输出False
print(8!=6) #输出True
print(1<2<3) #输出True
print(5>4>3) #输出True
print(5>4<3) #输出False
print(4==4>3) #输出True
a=8
b=8
print("相等吗？",a==b) #输出True
print("对象相同吗？",a is b) #输出True
import time  #引入time模块
t1 = time.gmtime() # gmtime()用来获取当前时间
t2 = time.gmtime() # gmtime()用来获取当前时间
print("相等吗？",t1 == t2) #输出True，程序运行快， t1和t1的时间一样
print("对象相同吗？",t1 is t2) #输出False每次调用gmtime()都返回不同对象