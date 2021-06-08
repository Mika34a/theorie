# output.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements functionality to create output.

# import
from sys import argv

#

def output(connections_dict, Smartgrid):
    """
    Gives output information about solution.
    """
    # district number
    print("Case information---------------------")
    print("district ", argv[2])
    # costs
    print("Total costs: ", Smartgrid.costs(Smartgrid, connections_dict))
    # battery location (x,y)
    print("Battery information-----------------")
    for connection in connections_dict.values:
        print("Location: ", connection.battery.x_coordinate, connection.battery.y_coordinate) 
        print("Capacity: ", connection.battery.capacity)
        # houses 
        print("Houses information-----------------")
        print("Location: ", connection.house.x_coordinate, connection.house.y_coordinate)
        print("output: ", connection.house.output)
        # points (x,y)
