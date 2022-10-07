import numpy as np
import matplotlib.pyplot as plt
import math

# Task 2 Lab1

#  %%-----------------------------------------
p = np.linspace(start=-5, stop=5, num=100)


#  %%-----------------------------------------
def radbas(n):
    return np.exp(-2 * n)


def dradbas(n):
    return -2 * n * np.exp(-2 * n)


t_radbas = radbas(p)
t_dradbas = dradbas(p)

plt.xlabel('x')
plt.ylabel('y')
plt.title("Radbas(blue), Dradbas(green)")
plt.plot(p, t_radbas, 'g')
plt.plot(p, t_dradbas, 's')
plt.title('radbas Function')
plt.show()


def writeToFile():
    print('radbas Function')
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\Readme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = radbas(i)
            print("x= ", i, "y=", t, file=f1)
            print("x=", i, "y=", t)


def writeToFileD():
    print('Dradbas Function')
    with open('D:\Політех\ІІ курс\Методи штучного інтелекту\Lab\Lab 1\DReadme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = dradbas(i)
            print("x= ", i, "y=", t, file=f1)
            print("x= ", i, "y=", t)


writeToFile()
writeToFileD()
