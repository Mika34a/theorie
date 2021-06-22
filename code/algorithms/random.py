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

        houses_list = []
        for house in smartgrid.houses_dict.values():
            houses_list.append(house)
            random.shuffle(houses_list)

        batteries_list = []
        for battery in smartgrid.batteries_dict.values():
            batteries_list.append(battery)
            random.shuffle(batteries_list) 

        for house in houses_list:    
            # check if output of house still fits in capacity battery 
            for battery in batteries_list:
                
                # connect house to battery 
                if  house.output <= battery.capacity:
                    # check if house is already connected
                    if house.connected == False:
                        connection = smartgrid.connect(battery, house)

                        # update battery capacity
                        smartgrid.output_capacity(house, battery)

                        # put connection in dict
                        connections_dict[connection.house] = connection

        # all_connected                
        if smartgrid.all_connected(connections_dict):
            # print(f"dict len: {len(connections_dict)}") 
            return connections_dict
        else:
            for battery in batteries_list:
                battery.reset()
            for house in houses_list:
                house.reset()
            continue   





