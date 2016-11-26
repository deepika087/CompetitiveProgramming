import matplotlib.pyplot as plt
import random
import math

def drawScatter():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [3, 4, 5, 6, 1, 2, 3, 4, 5]

    plt.scatter(x, y, label='This is my scatter plot', color='c')

    plt.xlabel('This is label x')
    plt.ylabel('This is label y')
    plt.title('This is my custom label')
    plt.legend()
    plt.show()

def drawRandomDataScatter():
    x = []
    y = []
    for i in range(1000):
        x.append(round(random.gauss(0, math.sqrt(1)), 3))
        y.append(round(random.gauss(0, math.sqrt(1)), 3))

    #print "x = ", x, " y = ", y
    plt.scatter(x, y, label='This is my scattered plot', color='c')
    plt.xlabel('This is label x')
    plt.ylabel('This is label y')
    plt.title('This is the title')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    #drawScatter()
    drawRandomDataScatter()