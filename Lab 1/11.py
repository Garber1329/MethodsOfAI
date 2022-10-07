import matplotlib.pyplot as plt
import numpy as np
import math


def compet(n):
    """
    Competitive
    """
    x = np.copy(n)
    x[x == 1] = 1
    x[x > 1] = 0
    x[x < 1] = 0
    return 1


def tr(n):
    return np.where(n == 1, 1, 0)


p = np.linspace(start=-5, stop=5, num=5)
t = compet(p)

plt.title('Compet(blue)')
plt.xlabel("x")
plt.ylabel("y")
plt.bar(p, t)
plt.show()


def writeToFileCompet():
    print('Compet() Function')
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\Readme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = compet(i)
            print("x= ", i, "y=", t, file=f1)
            print("x=", i, "y=", t)


writeToFileCompet()
