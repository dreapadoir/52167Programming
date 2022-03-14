#program to plot salaries
#Author: David Higgins

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10
np.random.seed(1)

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

print(salaries)

salariesPlus = salaries + 5000

print(salariesPlus)

salariesMult = salaries * 1.05

newSalaries = salariesMult.astype(int)

print(newSalaries)

plt.hist(salaries)
plt.show()