def info(name, score1, score2):
    print("姓名：{} 成绩1：{:.1f} 成绩2：{:.1f}".format(name, score1,
                                               score2))

info("小空", 70, 92)  # 参数数量、位置、参数类型都一致
info("小朱", 60)  # 参数位置、类型一致，数量不一致，语法错误
info("小沙", 80, "90")  # 参数位置、数量一致，类型不一致，语法错误
