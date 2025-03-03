from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 输入测试集
mydata = {'x': [1,3,7,2,5], 'y': [4,9,19,8,10]}
mydata_frame = pd.DataFrame(mydata)
x = mydata_frame['x'].values.reshape(-1, 1)
y = mydata_frame['y']

depth = np.arange(1, 15)

scores = []
for i in depth:
    model = DecisionTreeRegressor(max_depth=i)
    model.fit(x, y)
    score = model.score(x, y)
    scores.append(score)

# plt.plot(depth, scores, 'o-')
# plt.rcParams['font.sans-serif'] = 'Microsoft Yahei'
# plt.xlabel('决策树的深度')
# plt.ylabel('预测准确率')
# plt.show()
# 决策树深度为4的模型
model = DecisionTreeRegressor(max_depth=3)
model.fit(x, y)
plt.scatter(x, y) # 画出散点图
x_test = np.arange(0, 10.0, 0.01).reshape(-1, 1)
plt.plot(x_test, model.predict(x_test))
plt.rcParams['font.sans-serif'] = 'Microsoft Yahei'
plt.xlabel('x')
plt.ylabel('y')
plt.show()
