#program to plot salaries
#Author: David Higgins

from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10
np.random.seed(1)

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low = 20, high = 65, size = numberOfEntries)

#print(salaries)

#salariesPlus = salaries + 5000

#print(salariesPlus)

#salariesMult = salaries * 1.05

#newSalaries = salariesMult.astype(int)

#print(newSalaries)

#plt.hist(salaries)
#plt.show()

plt.scatter(ages, salaries, label = 'salaries')
#plt.show()

xpoints = np.array(range(0,101))
ypoints = xpoints ** 2

plt.plot(xpoints, ypoints, color = 'r', label = 'x_squared')
plt.title('random plot')
plt.xlabel('salaries')
plt.ylabel('age')
plt.legend()
plt.show()