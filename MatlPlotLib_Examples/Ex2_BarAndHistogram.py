
import matplotlib.pyplot as plt

def drawHistogram():
    #Now rather than having len(population_ages) number of groups you will have len(bins) number of groups
    population_ages =[12, 45, 67, 13, 90, 11, 56, 71, 23, 45, 62, 89, 92, 12, 11, 1, 0, 4, 5, 6, 7, 22,23, 51, 6, 100]
    bins = [0, 10, 20 , 30 , 40, 50 , 60 , 70 , 80, 90, 100]

    plt.hist(population_ages, bins, histtype='bar', rwidth=0.6) #control the width of the bars plot

    plt.xlabel('This is label x')
    plt.ylabel('This is label y')

    plt.title('This is the title for bar graph')
    plt.show()

def drawBar():
    x = [1, 4, 5, 6, 7]
    y = [2, 5, 9, 11, 10]

    x2 = [1, 3, 5, 7, 8]
    y2 = [1, 2, 3, 4, 5]

    plt.bar(x, y, label = "Bar1", color='red')
    plt.bar(x2, y2, label = "Bar2", color='c') #c for cyan. Without color all the bars will be of same color.

    plt.xlabel('This is label x')
    plt.ylabel('This is label y')

    plt.title('This is the title for bar graph')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    #drawBar()
    #drawHistogram()

    myList = ["deepika", "anand", "Ex"]
    for i in range(len(myList)):
        print " Val = ", myList[i], " for i = ", i
        myList.append("Buggy value")
        print " Updated list = ", myList