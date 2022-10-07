import numpy as np
import matplotlib.pyplot as plt

# Task 4 Lab1

#  %%-----------------------------------------
p = np.linspace(start=-5, stop=5, num=100)


#  %%-----------------------------------------

def poslin(n):
    return np.where(n < 0.0, 0, n)


def dposlin(n):
    return np.where(n < 0.0, 0, 1)

t = poslin(p)
plt.plot(p, t, ls='-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Poslin Function')
plt.show()
#  %%-----------------------------------------

d = dposlin(p)
plt.plot(p, d, ls='-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dposlin Function')
plt.show()


#  %%-----------------------------------------


def writeToFilePoslin():
    print('PoslinFunction')
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\Readme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = poslin(i)
            print("x= ", i, "y=", t, file=f1)
            print("x=", i, "y=", t)


writeToFilePoslin()


def writeToFileDposlin():
    print('Dposlin Function')
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\DReadme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = dposlin(i)
            print("x= ", i, "y=", t, file=f1)
            print("x= ", i, "y=", t)


writeToFileDposlin()
