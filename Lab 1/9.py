import matplotlib.pyplot as plt
import numpy as np
import math


def logsig(x):
    return 1 / (1 + np.exp(-x))


def dlogsign(x):
    return np.exp(-x) / (pow((1 + np.exp(-x)), 2))


x = np.linspace(-5, 5, 10)
p = logsig(x)
r = dlogsign(x)

plt.title('Logsing(blue), dlogsign(red)')
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.plot(x, p)
plt.plot(x, r)
plt.show()


def writeToFileLogsig():
    print('logsign(x) Function')
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\Readme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = logsig(i)
            print("x= ", i, "y=", t, file=f1)
            print("x=", i, "y=", t)


writeToFileLogsig()


def writeToFileDlogsig():
    print('Dlogsign(x) Function')
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\DReadme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = dlogsign(i)
            print("x= ", i, "y=", t, file=f1)
            print("x= ", i, "y=", t)


writeToFileDlogsig()
