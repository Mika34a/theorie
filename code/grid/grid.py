import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

plt.style.use('_classic_test_patch')

figure(figsize=(10, 10), dpi=150)

# see every step of grid and in graph
tick_spacing = 1
fig, ax = plt.subplots(1,1)

# major ticks every 10, minor ticks every 5
major_ticks = np.arange(0, 51, 10)
minor_ticks = np.arange(0, 51, 1)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

# background colour
ax.set_facecolor('xkcd:charcoal')

# grid
ax.grid(which='minor', alpha=0.2, color = 'w', linestyle = '-')
ax.grid(which='major', alpha=0.5, color = 'w', linestyle = '-')

# points set to always show full graph
plt.plot(0, 0)
plt.plot(50, 50)

# set specific point
plt.plot(34,47, 'bo')

# save as image
plt.savefig("grid")