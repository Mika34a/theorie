# random.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements a random algorithm to connect houses to batteries with capacity. 

# import 
from  ..classes import *
from code.classes import *
from smartgrid import Smartgrid
import random

def random_connections(houses_dict, batteries_dict):
    valid = True

    while valid == True:
        # dinctionary of connections
        connections_dict = {}

        houses_list = []
        for house in houses_dict.values():
            houses_list.append(house)
            random.shuffle(houses_list)

        batteries_list = []
        for battery in batteries_dict.values():
            batteries_list.append(battery)
            random.shuffle(batteries_list)

        for house in houses_list:    
            # check if output of house still fits in capacity battery 
            for battery in batteries_list:
                
                # connect house to battery 
                if  house.output <= battery.capacity:
                    connection = Smartgrid.connect(Smartgrid, battery, house)
                    Smartgrid.output_capacity(Smartgrid, house, battery)# make function in smartgrid

                    # put connection in dict
                    connections_dict[connection.house] = connection
                    

        for house in houses_list:
            not_connected = []
            if house.connected == False:
                not_connected.append(house)

        if len(not_connected) != 0:
            for house in houses_list:
                    house.connected = False
            continue
        else:
            print(f"dict len: {len(connections_dict)}") 
            return connections_dict       





