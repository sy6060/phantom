import numpy as np
import matplotlib.pyplot as plt
np.arange(1,22)
x = np.arange(1,22)
y = 2*x + 5
plt.plot(x, y)
plt.title("line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y)
plt.show()