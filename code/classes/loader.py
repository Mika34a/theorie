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
from .battery import Battery
from .connection import Connection

def load():

    # make empty houses dict
    houses_dict = {}
    id = 0

    # load houses
    with open('database/district_1/district-1_houses.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        # skip first line
        next(plots)
        for row in plots:
            
            # make house
            house = House(row[0], row[1], row[2], False, id)

            # put house in dict
            houses_dict[house.id] = house
            id += 1
            print(house)

    # load batteries

    # make empty batteries dict
    batteries_dict = {}
    id = 0
    
    with open('database/district_1/district-1_batteries.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        # skip first line
        next(plots)

        # loop through lines
        for row in plots:

            # get coordinates 
            coordinates = row[0].split(",")
            print(coordinates)

            # make battery
            battery = Battery(coordinates[0], coordinates[1], row[1], id)

            # put battery in dict
            batteries_dict[battery.id] = battery
            id += 1
        print(batteries_dict)    
            
    # load connections
    return houses_dict