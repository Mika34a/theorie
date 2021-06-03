import numpy as np
import matplotlib.pyplot as plt



grid = []
for row in range(50):
    for col in range(50):
        grid.append([row, col])


plt.grid(color = 'green', linestyle = '-', linewidth = 0.5)

plt.savefig("test")