import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv

plt.style.use('seaborn-pastel')

figure(figsize=(9, 9), dpi=150)

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

# loop for houses
with open('database/district_1/district-1_houses.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first line
    next(plots)
    for row in plots:
        plt.plot(int(row[0]), int(row[1]), 'o')

# loop for batteries, each battery own colour
with open('database/district_1/district-1_batteries.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first line
    next(plots)
    battery = 0
    for row in plots:
        # cleanup datafile
        x_cor, y_cor = row[0].split(',')
        plt.plot(int(x_cor), int(y_cor), 'Pr')
        battery += 1
        
        if battery == 1:
            plt.plot(int(x_cor), int(y_cor), 'Pm')
        elif battery == 2:
            plt.plot(int(x_cor), int(y_cor), 'Pg')
        elif battery == 3:
            plt.plot(int(x_cor), int(y_cor), 'Pb')
        elif battery == 4:
            plt.plot(int(x_cor), int(y_cor), 'Pw')

# save as image
plt.savefig("grid")