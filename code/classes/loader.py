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

def load_house():

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
            house = House(int(row[0]), int(row[1]), float(row[2]), False, id)

            # put house in dict
            houses_dict[house.id] = house
            id += 1

    return houses_dict

    # load batteries

def load_bat():
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

            # make battery
            battery = Battery(int(coordinates[0]), int(coordinates[1]), row[1], id)

            # put battery in dict
            batteries_dict[battery.id] = battery
            id += 1
            
    # load connections
    return batteries_dict