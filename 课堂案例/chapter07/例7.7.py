def TVinfo(TVname, TVnum, playName='西游记'):
    "打印任何传入的字符串"
    print("电视台：{} 台号：{} 剧名：{}".format(TVname, TVnum, playName))

# 调用TVinfo函数
TVinfo(TVname="CCCV", TVnum=15)
TVinfo(TVname="Jaimin", playName='三国演义', TVnum=2)
