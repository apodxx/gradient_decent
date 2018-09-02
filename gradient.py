import matplotlib.pyplot as plt
#数据是我自己编的，故意编的很像一个单调递增的一次函数
x = [100,80,120,75,60,43,140,132,63,55,74,44,88]
y = [120,92,143,87,60,50,167,147,80,60,90,57,99]
#步长
alpha = 0.00001

cnt = 0
#计算样本个数
m = len(x)
#初始化参数的值，拟合函数为 y=theta0+theta1*x
theta0 = 0
theta1 = 0
#误差
error0=0
error1=0
#退出迭代的两次误差差值的阈值
epsilon=0.000001

#开始迭代
while True:
    diff = [0, 0]
    for i in range(len(x)):
        diff[0]+=(theta0+theta1*x[i]-y[i])
        diff[1]+=(theta0+theta1*x[i]-y[i])*x[i]
    theta0 -= alpha*diff[0]
    theta1 -= alpha*diff[1]

    error1=0
    for i in range(len(x)):
        error1+=(y[i]-theta0-theta1*x[i])**2/2
    if abs(error1-error0)<epsilon:
        break
    else:
        error0=error1

plt.plot(x,y,'bo')
print(theta1,theta0)
plt.show()