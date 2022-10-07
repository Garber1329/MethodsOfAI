import numpy as np
import matplotlib.pyplot as plt


def tansig(x):
    return 2 / ((1 + np.exp(-2 * x)) - 1)


def dtansig(x):
    return 1 - (pow(np.tan(x), 2))


x = np.linspace(-5, 5, 10)
p = tansig(x)

r = dtansig(x)

plt.title('Tansig(blue), dtansig(red)')
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, p)
plt.plot(x, r)
plt.show()


def writeToFileTansig():
    print('tansig(x) Function')
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\Readme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = tansig(i)
            print("x= ", i, "y=", t, file=f1)
            print("x=", i, "y=", t)


writeToFileTansig()


def writeToFileDtansig():
    print('Dtansig(x) Function')
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\DReadme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = dtansig(i)
            print("x= ", i, "y=", t, file=f1)
            print("x= ", i, "y=", t)


writeToFileDtansig()
