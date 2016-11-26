
import matplotlib.pyplot as plt

#Basic Plot
x1 = [11, 2, 3]
y1 = [4, 5, 16]

x2 = [4, 5, 6]
y2 = [2, 8, 1]

plt.plot(x1, y1, label='FirstLine')
plt.plot(x2, y2, label='Second Line')

#Legends and titles
plt.xlabel('This is x label')
plt.ylabel('This is y label')
plt.title('This is a fancy title')

plt.legend() #To display that box on the corner that red is this and blue is this

#Bar Chart
plt.show()