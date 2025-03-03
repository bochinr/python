file = open(r"/chapter10/data.txt", "r", encoding="utf-8")
res = file.read(10)
print(res)
file.close()