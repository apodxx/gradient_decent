import matplotlib.pyplot as plt
#数据是我自己编的，故意编的很像一个单调递增的一次函数
x = [100,80,120,75,60,43,140,132,63,55,74,44,88]
y = [120,92,143,87,60,50,167,147,80,60,90,57,99]
error0=0
error1=1
eps=0.001
theta0=0
theta1=0

count=0
alpha=0.00001
def test(x):

    return x*theta1+theta0
def h(x):
    return theta1*x+theta0
while True:
    diff = [0, 0]
    count+=1
    for i in range(len(x)):
        diff[0]+=(theta0+theta1*x[i]-y[i])
        diff[1]+=(theta0+theta1*x[i]-y[i])*x[i]
    theta0 -= alpha*diff[0]
    theta1 -= alpha*diff[1]

    error1=0
    for i in range(len(x)):
        error1+=(y[i]-theta0-theta1*x[i])**2/2
    if abs(error1-error0)<eps:
        break
    else:
        error0=error1

plt.plot(x,[h(x) for x in x])
plt.plot(x,y,'bo')
plt.plot([110],[test(110)],'r+')
print(theta1,theta0)
plt.show()


