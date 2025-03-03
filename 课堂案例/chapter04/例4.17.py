while True:
    score= int(input("请输入你的成绩："))
    if score>90:
        print("成绩优异，为你骄傲！")
    elif score>80:
        pass
    elif score>70:
        print("成绩一般，需要加油！")
    else:
        print("成绩很差，需要加油加油再加油！")
        break