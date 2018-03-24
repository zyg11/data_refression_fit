#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#定义x、y散点坐标
# x = np.arange(1, 16, 1)
# x=[0.5,1,2.5,3,4,5,6,7]
# x=[0,0.0039,0.0067,0.00819,
#    0.0102,0.0121,0.015,0.0357,
#    0.0401,0.0419,0.0491,0.0523,0.0549,
#    0.0564,0.0641,0.0793,0.0795,
#    0.0877,0.1269,0.128,0.1318,
#    0.1707,0.256]
#导入数据及x、y散点坐标
data = pd.read_csv("F:/data-3.csv")
print(data)
x=data['x']
y=data['y']

# x=np.array(x)
# num = [4.00, 5.20, 5.900, 6.80, 7.34,
#        8.57, 9.86, 10.12, 12.56, 14.32,
#        15.42, 16.50, 18.92, 19.58, 20.00]
# num = [0,0.133333333333333, 0.266666666666667,0.115384615384615,
#        0.230769230769231,0.0555555555555556,0.166666666666667,0.346153846153846,
#        0.461538461538462,0.277777777777778,0.433333333333333,0.615384615384615,0.5,
#        0.388888888888889,0.6,0.769230769230769,0.555555555555556,
#        0.666666666666667,0.722222222222222,0.8,1,
#        1,1]
# y = np.array(y)

#用3次多项式拟合
f1 = np.polyfit(x, y, 3)
p1 = np.poly1d(f1)
print(p1)

#也可使用yvals=np.polyval(f1, x)
yvals = p1(x)  #拟合y值

#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='fit values')
# text=u'频率下降频率 τ'
plt.xlabel('τ')
plt.ylabel('H')
# plt.legend(loc=4) #指定legend的位置右下角
# plt.title('polyfitting')
plt.show()
# plt.savefig('test.png')