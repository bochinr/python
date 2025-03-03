import os
res = os.walk(r"F:\Python\Code\chapter10\test10")
count = 1
for root, dirs, files in res:
    print("******%d******" % count)
    count += 1
    print("root:" + root)
    for name in dirs:
        print(os.path.join(root, name))
    for name in files:
        print(os.path.join(root, name))