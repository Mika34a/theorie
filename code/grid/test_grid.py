import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

for n in range(50):
    x.append(n)
    y.append(n)

np.asarray(x)
np.asarray(y)

plt.grid(color = 'green', linestyle = '-', linewidth = 1)

plt.savefig("test")