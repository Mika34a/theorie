# greedy_random_shared.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements a greedy random algorithm to connect houses to batteries
# - connections are shared between houses if more efficient.
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
            # a dictionary of batteries based on proximity
            batteries_closest = smartgrid.proximity(house, smartgrid.batteries_dict)
                    
            # first loop through batteries starting closest one
            for battery in batteries_closest:

                if smartgrid.near_connection(house, battery, connections_dict) != False:
                    # find closest coordinate of connection to battery
                    close_connection_coordinate = smartgrid.near_connection(house, battery, connections_dict)
                    
                    x_connect = close_connection_coordinate[0]
                    y_connect =  close_connection_coordinate[1]

                    dist_connection = smartgrid.distance(x_connect, y_connect, house)
                    dist_battery = smartgrid.distance(battery.x_coordinate, battery.y_coordinate, house)

                    # connect house to battery 
                    if  house.output <= battery.capacity:
                    # check if house is already connected
                        if house.connected == False:
                            if dist_connection < dist_battery:
                                connection = smartgrid.connect(x_connect, y_connect, battery, house)
                            else:
                                connection = smartgrid.connect(battery.x_coordinate, battery.y_coordinate, battery, house)          
                else:
                    # connect house to battery 
                    if  house.output <= battery.capacity:
                        # check if house is already connected
                        if house.connected == False:
                            connection = smartgrid.connect(battery.x_coordinate, battery.y_coordinate, battery, house)  

            # update battery capacity
            smartgrid.output_capacity(house, battery)

            # put connection in dict
            connections_dict[connection.house] = connection
            print(len(connections_dict))
        
        # check if all houses are connected               
        if smartgrid.all_connected(houses_list, connections_dict):
            print(f"dict len: {len(connections_dict)}") 
            return connections_dict
        else:
            print("False")
            # if not reset everything and re-iterate
            for battery in batteries_closest:
                battery.reset()
            for house in houses_list:
                house.reset()
            continue   
