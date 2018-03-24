from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import caffe
#导入数据
data=pd.read_csv("data_mishu.csv")
xdata=data['X']
ydata=data['Y']
def func(x, a):
    return x**a



popt, pcov = curve_fit(func, xdata, ydata)
# popt数组中，三个值分别是待求参数a,b,c
y2 = [func(i, popt[0]) for i in xdata]
plot1=plt.plot(xdata, ydata, 's',label='original values')
plot2=plt.plot(xdata, y2, 'r',label='fit values')
plt.xlabel('τ')
plt.ylabel('H')
# plt.legend(loc=4)
print(popt)
plt.show()