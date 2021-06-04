# loader.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements loader.

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv
from .house import House

def load():

    # make empty houses dict
    houses_dict = {}

    # load houses
    with open('database/district_1/district-1_houses.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:

            # plot
            plt.plot(row[0], row[1], 'o')

            # make house
            house = House(row[0], row[1], row[2], False)

            # put house in dict
            houses_dict [house.id] = house

    # load batteriespython
    with open('database/district_1/district-1_batteries.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            print(row)

    # load connections
    return houses_dict