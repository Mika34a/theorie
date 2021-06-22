import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv

def create_grid(houses, batteries, connections):
    """
    Creates a png grid visualistion of all houses, batteries
    and connections.
    """
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
    
    # plot the connection lines per battery 
    for bat in batteries.values():
        if bat.id == 0:
            
            for connection in connections.values():
                if connection.battery_id == bat:
                    plt.plot(connection.points_x, connection.points_y, "r")
            
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'sr')
        elif bat.id == 1:
            
            for connection in connections.values():
                if connection.battery_id == bat:
                    plt.plot(connection.points_x, connection.points_y, "m")
            
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'sm')
        elif bat.id == 2:
            
            for connection in connections.values():
                if connection.battery_id == bat:
                    plt.plot(connection.points_x, connection.points_y, "g")
            
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'sg')
        elif bat.id == 3:
            
            for connection in connections.values():
                if connection.battery_id == bat:
                    plt.plot(connection.points_x, connection.points_y, "b")
            
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'sb')
        elif bat.id == 4:
            
            for connection in connections.values():
                if connection.battery_id == bat:
                    plt.plot(connection.points_x, connection.points_y, "w")
            
            # plot the battery
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'sw')
    
    # plot the houses
    for house in houses.values():
        plt.plot(house.x_coordinate, house.y_coordinate, 'o')

    # save as image
    plt.savefig("code/grid/gridtest.png")