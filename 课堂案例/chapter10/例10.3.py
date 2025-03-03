import os
path = "myDir"
if not os.path.exists(path):
    os.mkdir(path)
else:
    print(path + "目录已经存在，不能重复创建!")