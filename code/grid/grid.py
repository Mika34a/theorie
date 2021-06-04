import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv

plt.style.use('seaborn-pastel')

figure(figsize=(10, 10), dpi=150)

# see every step of grid and in graph
tick_spacing = 1
fig, ax = plt.subplots(1,1)

# major ticks every 10, minor ticks every 5
major_ticks = np.arange(0, 51, 10)
minor_ticks = np.arange(0, 51, 1)

ax.set_autoscale_on(False)

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

# loop for houses
with open('database/district_1/district-1_houses.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots)
    for row in plots:
        plt.plot(int(row[0]), int(row[1]), 'o')

# save as image
plt.savefig("grid")