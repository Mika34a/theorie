import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv

def create_grid(houses, batteries):
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

    for house in houses.values():
        plt.plot(house.x_coordinate, house.y_coordinate, 'o')

    battery = 0

    for bat in batteries.values():
        if battery == 0:
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'Pr')
        elif battery == 1:
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'Pm')
        elif battery == 2:
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'Pg')
        elif battery == 3:
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'Pb')
        elif battery == 4:
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'Pw')
        battery += 1

    # save as image
    plt.savefig("code/grid/grid.png")