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

def random_connections(houses_dict, batteries_dict):
    # dinctionary of connections
    connections_dict = {}

    # loop through houses
    for house in houses_dict.values():
        
        # check if output of house still fits in capacity battery 
        for battery in batteries_dict.values():
            
            # connect house to battery 
            if  house.output <= battery.capacity:
                connection = Smartgrid.connect(Smartgrid, battery, house)
                battery.capacity = battery.capacity - house.output # make function in smartgrid

                # put connection in dict
                connections_dict[connection.house] = connection
    return connections_dict             





