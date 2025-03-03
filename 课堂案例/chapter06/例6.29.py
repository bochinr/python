user_info = {"Jaimin": "wjm123",
             "Lucy": "lc123",
             "James": "js123",
             "Nancy": "nc123",
             "Alice": "al123"}
i = 1
while i <= 3:
    user_name = input("请输入用户名：")
    user_pwd = input("请输入密码：")
    if user_name in user_info.keys():
        if user_pwd == user_info[user_name]:
            print("登录成功！")
            break
        else:
        print("密码错误！")
    else:
        print("用户名不存在！")
    i = i + 1
    else:
        print("尝试登录超过三次，请稍后再试！")
