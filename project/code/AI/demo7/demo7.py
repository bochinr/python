import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter

data = pd.read_csv("./unprocess.csv", encoding="GBK")  # 读取数据
print(data.head(10))  # 显示数据前十行
print(data.info())  # 显示数据信息

print(data.isnull().any())  # 查看缺失值
print(data[data.isnull().values == True])  # 查看缺失值的完整数据
data.dropna(subset=["text_a", "label"], axis=0, how="any", inplace=True)  # 删除缺失值
print(data.isnull().any())  # 再次查看缺失值

print(data[data.duplicated("text_a")])  # 查看重复值
data.drop_duplicates(subset=["text_a"], keep="first", inplace=True)  # 删除重复值
print(data[data.duplicated("text_a")])  # 再次查看重复值

# 绘制箱线图
plt.boxplot(x=data.label,
            whis=1.5,
            widths=0.7,  # 指定箱线图的宽度为0.7磅
            patch_artist=True,  # 指定箱体需要填充颜色
            showmeans=True,  # 指定需要显示均值
            boxprops={'facecolor': 'steelblue'},  # 指定箱体的填充色为铁蓝色
            # 指定异常值的填充色、边框色和大小
            flierprops={'markerfacecolor': 'red', 'markeredgecolor': 'red', 'markersize': 4},
            # 指定均值点的标记符号（菱形）、填充色和大小
            meanprops={'marker': 'D', 'markerfacecolor': 'black', 'markersize': 4},
            medianprops={'linestyle': '--', 'color': 'orange'},  # 指定中位数的标记符号（虚线）和颜色
            labels=['']  # 去除箱线图的x轴刻度值
            )
# 显示图形
plt.show()

# 计算下四分位数和上四分位数
Q1 = data.label.quantile(q=0.25)
Q3 = data.label.quantile(q=0.75)

# 基于1.5倍的四分位差计算上、下须对应的值
low_whisker = Q1 - 1.5 * (Q3 - Q1)
up_whisker = Q3 + 1.5 * (Q3 - Q1)

# 寻找异常值点
data2 = data.label[(data.label > up_whisker) | (data.label < low_whisker)]

# 统计异常值点
print(Counter(data2))

print(data[data["label"] == 6.0])  # 查找异常数据
data.drop((data[data["label"] == 6.0]).index, inplace=True)  # 删除异常数据
print((data["label"] == 6.0).any())  # 检查是否有异常数据

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置标签
labels = ['消极', '积极']

# 设置数值
sizes = [320, 682]

# 绘制图像
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

# 设置图像标题
ax.set_title('各种情绪的比例')

# 展示图像
plt.show()
