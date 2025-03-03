#将百分制成绩转换成五分制
score=float(input(" 请输出一个百分制成绩："))
if score>=90.0:
    grade="A"
elif score>=80.0:
    grade="B"
elif score>=70.0:
    grade="C"
elif score>=60.0:
    grade="D"
else:
    grade="E"
print("对应的五分制成绩是：{}".format(grade))
