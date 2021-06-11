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

        # initialise randomised list of batteries
        batteries_list = []
        for battery in smartgrid.batteries_dict.values():
            batteries_list.append(battery)
            random.shuffle(batteries_list)

        for house in houses_list:    
            # first loop through batteries to find the closest one
            for battery in batteries_list:

                # function that orders the batteries in a list 
                
                # connect house to battery 
                if  house.output <= battery.capacity:
                    # check if house is already connected
                    if house.connected == False:
                        connection = smartgrid.connect(battery, house)

                        # update battery capacity
                        smartgrid.output_capacity(house, battery)

                        # put connection in dict
                        connections_dict[connection.house] = connection
        
        # check if all houses are connected               
        if smartgrid.all_connected(houses_list, connections_dict):
            print(f"dict len: {len(connections_dict)}") 
            return connections_dict
        else:
            # if not reset everything and re-iterate
            for battery in batteries_list:
                battery.reset()
            for house in houses_list:
                house.reset()
            continue   
