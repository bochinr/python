from sklearn.linear_model import LinearRegression,SGDRegressor
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = {"s": [100, 90, 60, 50, 55], "p": [301, 285, 200, 300, 180]}


# In[3]:


data_frame = pd.DataFrame(data)


# In[4]:


#获取训练集
x = data_frame["s"].values.reshape(-1, 1)



# In[5]:


y = data_frame["p"]



# In[6]:


#创建模型
model1 = LinearRegression()
model2 = SGDRegressor(loss='huber', max_iter=5000)


# In[7]:


#训练模型
model1.fit(x, y)
model2.fit(x, y)


# In[11]:


# 预测
y1 = model1.predict(x)
y2 = model2.predict(x)


# In[19]:


plt.scatter(x, y)
plt.scatter(x, y1)
plt.scatter(x, y2,)
plt.show()

# In[14]:


plt.plot(x, y1, "g")
plt.plot(x, y2)
plt.show()

