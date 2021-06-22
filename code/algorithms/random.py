# random.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements a random algorithm to connect houses to batteries with capacity. 

import random

def run(smartgrid):
    """
    Runs the random algorithm.
    """
    while True:
        # dictionary of connections
        connections_dict = {}

        # initialise randomised list of houses
        houses_list = []
        for house in smartgrid.houses_dict.values():
            houses_list.append(house)
            random.shuffle(houses_list)

        # initialise randomised list of batteries
        batteries_list = []
        for battery in smartgrid.batteries_dict.values():
            batteries_list.append(battery)
            random.shuffle(batteries_list) 

        for house in houses_list:    
            for battery in batteries_list:
                # check if battery capacity can host house
                if  house.output <= battery.capacity:
                    # check if house isn't already connected
                    if house.connected == False:
                        connection = smartgrid.connect(battery, house)

                        # update battery capacity
                        smartgrid.output_capacity(house, battery)

                        # put connection in dict
                        connections_dict[connection.house] = connection

        # check if all are connected                
        if smartgrid.all_connected(connections_dict):
            return connections_dict
        else:
            for battery in batteries_list:
                battery.reset()
            for house in houses_list:
                house.reset()
            continue   





