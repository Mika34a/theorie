import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv

def create_grid(houses, batteries, connections):
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

    for bat in batteries.values():
        if bat.id == 0:
            
            for connection in connections.values():
                if connection.battery_id == bat:
                    for point in connection.points_list:
                        plt.plot(point[0], point[1], "^r")
            
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'Pr')
        elif bat.id == 1:
            
            for connection in connections.values():
                if connection.battery_id == bat:
                    for point in connection.points_list:
                        plt.plot(point[0], point[1], "^m")
            
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'Pm')
        elif bat.id == 2:
            
            for connection in connections.values():
                if connection.battery_id == bat:
                    for point in connection.points_list:
                        plt.plot(point[0], point[1], "^g")
            
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'Pg')
        elif bat.id == 3:
            
            for connection in connections.values():
                if connection.battery_id == bat:
                    for point in connection.points_list:
                        plt.plot(point[0], point[1], "^b")
            
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'Pb')
        elif bat.id == 4:
            
            for connection in connections.values():
                if connection.battery_id == bat:
                    for point in connection.points_list:
                        plt.plot(point[0], point[1], "^w")
            
            plt.plot(bat.x_coordinate, bat.y_coordinate, 'Pw')

    # loop through every connection
    # save all the points of a connection and make them invisible
    # plot lines between each connection, based on battery colour
    # draw the lines
    # for connection in connections.values():
    #             for point in connection.points_list:
    #                 plt.plot(point[0], point[1], ",r")

    # save as image
    plt.savefig("code/grid/gridtest.png")