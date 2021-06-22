# greedy_random.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements a greedy random algorithm to connect houses to batteries
# with the algorithm preferencing the batteries that are closest by first.

import random

def run(smartgrid):

    while True:
        # dictionary of connections
        connections_dict = {}

        # initialise randomised list of houses
        houses_list = []
        for house in smartgrid.houses_dict.values():
            houses_list.append(house)
            random.shuffle(houses_list)

        for house in houses_list:    
            # a dictionary of batteries ordered by proximity
            batteries_closest = smartgrid.proximity(house, smartgrid.batteries_dict)
                    
            # first loop through batteries starting closest one
            for battery in batteries_closest:
                if  house.output <= battery.capacity:
                    # check if house is already connected
                    if house.connected == False:
                        connection = smartgrid.connect( battery, house)

                        # update battery capacity
                        smartgrid.output_capacity(house, battery)

                        # put connection in dict
                        connections_dict[connection.house] = connection
        
        # check if all houses are connected               
        if smartgrid.all_connected(connections_dict):
            return connections_dict
        else:
            # if not, reset everything and re-iterate
            for battery in batteries_closest:
                battery.reset()
            for house in houses_list:
                house.reset()