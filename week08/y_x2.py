#program to plot the function y = x^2
#Author: David Higgins

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(0,101))
ypoints = xpoints ** 2

plt.plot(xpoints, ypoints)
plt.show()