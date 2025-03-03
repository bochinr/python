import random

interest_groups = [[], [], []]
student_names = ["小明", "小花", "小丽", "张三", "李四", "小孙", "小朱"
    , "小沙"]
for i in student_names:
    n = random.randint(0, 2)
    interest_groups[n].append(i)
print("三个兴趣小组随机分配的小组成员结果为：")
for i in interest_groups:
    print(i)
