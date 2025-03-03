import json

try:
    f = open("学生信息查询表.txt", 'r', encoding='utf-8')
    content = f.read()
    try:
        content_dict = json.loads(content)  # 转换为字典类型
        address = input('请输入学生学号:')
        for key, val in content_dict.items():
            if key == address:
                print(val)
        f.close()
    except:
        print("文件格式转换失败，无法打开文件")
        raise
except FileNotFoundError:
    print("文件不存在")
