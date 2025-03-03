import os
path1 = r"F:\python"
path2 = r"demo"
path3 = r"myproject.txt"

path = os.path.join(path1, path2, path3)
print(path)