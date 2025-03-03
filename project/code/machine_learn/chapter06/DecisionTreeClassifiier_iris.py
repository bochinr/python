from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from matplotlib import pyplot as plt

mydata = datasets.load_iris()

x = mydata.data[:, 2:4]
y = mydata.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=50, random_state=0)

from sklearn.tree import DecisionTreeClassifier
# 决策树深度和预测准确率计算
depth = np.arange(1, 15)
scores = []
for i in depth:
    model = DecisionTreeClassifier(criterion='entropy', max_depth=i)
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    scores.append(score)

index = np.argmax(scores) # 获取预测准确率最大值的下标
print(depth[index]) # 得到预测准确率最大值对应的深度值
plt.plot(depth, scores,'o-')
plt.rcParams['font.sans-serif'] = 'Microsoft Yahei'
plt.xlabel('决策树深度')
plt.ylabel('预测准确率')
plt.show()


# 构建深度为3的决策树模型
model = DecisionTreeClassifier(criterion='entropy', max_depth=3)
model.fit(x_train, y_train)
# 模型评估
score = model.score(x_test, y_test)
print(score)

# 可视化图像，并现实分类效果
from matplotlib.colors import ListedColormap
N, M = 500, 800 # 定义网格采样点
t1 = np.linspace(0, 8, N) # 生成采样点的横坐标值
t2 = np.linspace(0, 5, M) # 生成采样点的纵坐标值
x1, x2 = np.meshgrid(t1, t2) # 生成网格采样点
x_new = np.stack((x1.flat,x2.flat), axis=1)  # 将采样点作为测试点
y_predict = model.predict(x_new) # 预测测试点的值
y_hat = y_predict.reshape(x1.shape) # 设置与 x1 相同的形状
iris_cmap = ListedColormap(["#ACF080", "#A0A0FF", "#FF8080"])  # 设置分类界面的颜色

# 绘制分类界面
plt.pcolormesh(x1, x2, y_hat, cmap = iris_cmap)
plt.scatter(x[y==0, 0], x[y==0, 1], c="b", marker="o", s=60) # 绘制标签值为0 的样本点
plt.scatter(x[y==1, 0], x[y==1, 1], c="r", marker="^", s=60) # 绘制标签值为1 的样本点
plt.scatter(x[y==2, 0], x[y==2, 1], c="g", marker=".", s=60) # 绘制标签值为2 的样本点
plt.rcParams["font.sans-serif"] = "Microsoft Yahei"
plt.xlabel("花瓣长度")
plt.ylabel("花瓣宽度")
plt.show()