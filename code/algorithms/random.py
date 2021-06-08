# random.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements a random algorithm to connect houses to batteries with capacity. 

from  ..classes import *

def random_connections(houses_dict, batteries_dict):
# dinctionary of connections
connections_dict = {}

# loop through houses
    for house in houses_dict.values:
        
        # check if output of house still fits in capacity battery 
        for battery in batteries_dict.values:
            
            # connect house to battery 
            if  house.output <= battery.capacity:
                connection = connect(battery, house)

                # put connection in dict
                connections_dict[connection.house] = connection
    return connections_dict             





