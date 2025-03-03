"""
	好友系统
	增加
	删除
	修改
	查询
"""
# friend = ['张三', '李四', '王五']
friends = []
print("欢迎使用好友系统")
print("1：添加好友")
print("2：删除好友")
print("3：备注好友")
print("4：展示好友")
print("5：退出")
while True:
    num = int(input("请输入您的选项："))
    if num == 1:
        add_friend = input("请输入要添加的好友：")
        if add_friend not in friends:
            friends.append(add_friend)
            print('好友添加成功')
        else:
            print("好友已存在！，无需再添加")
    elif num == 2:
        del_friend = input("请输入删除好友姓名：")
        if del_friend in friends:
            friends.remove(del_friend)
            print("删除成功")
        else:
            print("删除失败，好友列表不存在该好友")
    elif num == 3:
        before_friend = input("请输入要修改的好友姓名：")
        after_friend = input("请输入修改后的好友姓名：")
        if before_friend in friends:
            friend_index = friends.index(before_friend)
            friends[friend_index] = after_friend
            print("备注成功")
        else:
            print("修改失败，好友列表不存在该好友")
    elif num == 4:
        if len(friends) == 0:
            print("好友列表为空")
        else:
            for i in friends:
                print(i)
    elif num == 5:
        break
