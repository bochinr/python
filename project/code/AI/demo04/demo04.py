import csv
import pandas as pd

# 文本数据加载及储存
with open('data/data.csv', 'w') as fp:
    # 传入文件句柄
    writer = csv.writer(fp)
    # 执行写入操作
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['100001', 'lisi', '30'])
    writer.writerow(['100002', 'wuwang', '110'])
    writer.writerow(['100003', 'qianliu', '70'])

# 使用csv.reader()函数加载data.csv文件
# with open('data/data.csv', newline='') as csvf:
#     rows = csv.reader(csvf)
#     for row in rows:
#         print(row)
#
# # 使用pandas库加载csv文件
# data = pd.read_csv('data/data.csv')
# print(data[:5])

# demo04 start
path = r"data/ANLP002_moods_classify8_unprocessed.xlsx"
# 将标签和数据分离
data = pd.read_excel(path, header = None, skiprows = 0)
label = pd.read_excel(path, header = None, skiprows = 0)
print(data[: 5])
print(label[: 5])
#数据切片
# d = data[100: 200]
# l = label[100: 200]
# 保存数据
# d.to_csv('data/data_save.csv')
# l.to_csv('data/label_save.csv')