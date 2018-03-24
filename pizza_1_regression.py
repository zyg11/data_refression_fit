from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("E:/keras_data/linear_regression/pizza.csv")
print(data)
x=data['x']
y=data['y']
x=np.array(x).reshape(-1,1)
y=np.array(y).reshape(-1,1)
print(x)
print(y)
#回归
clf=linear_model.LinearRegression()#线性回归
t1=clf.fit(x,y)
res=clf.predict(np.array([12]).reshape(-1,1))[0]
print(u'预测一张12英寸匹萨价格：$%.2f' % res)

#预测结果
x2=[[0],[10],[14],[25]]
y2=clf.predict(x2)
print(u'系数',clf.coef_)
print(u'截距',clf.intercept_)
print(u'评分函数',clf.score(x,y))

#绘制线性回归图形
plt.figure()
plt.title(u'diameter-cost curver')   #标题
plt.xlabel(u'ediameter')              #x轴坐标
plt.ylabel(u'cost')                  #y轴坐标
plt.axis([0, 25, 0, 25])             #区间
plt.grid(True)                       #显示网格
plt.plot(x, y, 'k.')                 #绘制训练数据集散点图
plt.plot(x2, y2, 'g-')               #绘制预测数据集直线
plt.show()

