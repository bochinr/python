while True:
    rewardCard_info = ["谢谢惠顾", "一等奖", "三等奖", "谢谢惠顾", "谢谢惠顾", "三等奖", "二等奖", "谢谢惠顾"]
    num = int(input("请输入刮去的位置(1~8)："))
    if 0 <= num <= len(rewardCard_info):
        info = rewardCard_info[num - 1]
        print(f"{info}")
    else:
        print("卡片位置不合规！")
        break
