import matplotlib.pyplot as plt
import numpy as np
import math


def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)


def figure():
    scores = [0, 1.0, -0.5, 0.5]
    s = softmax(scores)
    plt.title('Softmax')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.bar(scores, s, color='maroon', width=0.4)
    plt.show()


def writeToFileFuncSoftmax():
    print('Softmax')
    scores = [0, 1.0, -0.5, 0.5]
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\Readme.txt', 'w') as f1:
        t = softmax(scores)
        print("x= ", scores, "t\ny=", t, file=f1)
        print("x=", scores, "\ny=", t)


figure()
writeToFileFuncSoftmax()
