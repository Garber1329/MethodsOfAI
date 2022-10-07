import numpy as np
import matplotlib.pyplot as plt

# Task 6 Lab1

#  %%-----------------------------------------
p = np.linspace(start=-5, stop=5, num=100)


#  %%-----------------------------------------
def satlins(n):
    x = np.copy(n)
    x[x <= 1]
    x[x >= 0]
    x[x > 1] = 1
    x[x < 0] = 0
    return x


def dsatlins(n):
    x = np.copy(n)
    x[x <= 1] = 1
    x[x >= 0] = 1
    x[x > 1] = 1
    x[x < 0] = 0
    return x


t = satlins(p)
plt.plot(p, t, ls='-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Satlins Function')
plt.show()
#  %%-----------------------------------------

d = dsatlins(p)
plt.plot(p, d, ls='-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dsatlins Function')
plt.show()


#  %%-----------------------------------------


def writeToFileSatlins():
    print('Satlin Function')
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\Readme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = satlins(i)
            print("x= ", i, "y=", t, file=f1)
            print("x=", i, "y=", t)


writeToFileSatlins()


def writeToFileDsatlins():
    print('Dsatlin Function')
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\DReadme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = dsatlins(i)
            print("x= ", i, "y=", t, file=f1)
            print("x= ", i, "y=", t)


writeToFileDsatlins()
