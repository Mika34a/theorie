# smartgrid.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements smartgrid class.

from code.classes import *
from code.classes.connection import Connection
from code.classes.house import House
from code.classes.battery import Battery
from code.algorithms import random
from code.output import output

class Smartgrid():
    def __init__(self, filename, filename2):
        """
        Initializes the Smartgrid class.
        """
        self.houses_dict= self.loader.load_house(filename)
        self.batteries_dict = self.loader.load_batteries(filename2) 

    def connect(self, battery, house):
        connection = Connection(house, battery)
        connection.add_point()
        house.connected = True
        return connection

    def costs(self, connections_dict, battery_dict):
        """
        Returns the total costs of the combined cables.
        """
        # laying a cable costs 9 per grid
        # costs for each battery is 5000
        COST_GRID = 9
        COST_BATTERY = 5000
        cost_cable_all = 0

        for con in connections_dict.values():
            cost_cable = con.length * COST_GRID
            cost_cable_all = cost_cable_all + cost_cable

        cost_battery_all = COST_BATTERY * len(battery_dict)
        cost_all = cost_cable_all + cost_battery_all
        return cost_all

    def disc_houses(self):
        """
        Returns the houses that have not been connected.
        """
        pass

    def batteries_left(self):
        """
        Returns the batteries that still have leftover capacity.
        """
        pass
    
    def output_capacity(self, house, battery):
        """
        Substracts the output from the house from the battery capacity.
        """
        battery.capacity = battery.capacity - house.output
        
    def output(self, connections_dict, total_cost):
        """
        Gives output information about solution.
        """
        # district number
        print("Case information---------------------")
        print("district ", argv[1])
        # costs
        print(f"Total costs: {total_cost}")
        # battery location (x,y)
        print("Battery information-----------------")
        for connection in connections_dict.values():
            print("Location: ", connection.battery.x_coordinate, connection.battery.y_coordinate) 
            print("Capacity: ", connection.battery.capacity)
            # houses 
            print("Houses information-----------------")
            print("Location: ", connection.house.x_coordinate, connection.house.y_coordinate)
            print("output: ", connection.house.output)
            # points (x,y)


if __name__ == "__main__":

    from code.classes import loader
    from code.grid import grid
    from sys import argv

    # check command line
    if len(argv) != 2:
        print("Usage: python3 smartgrid.py [district_number]")
        exit(1)
    # Load the requested files
    if len(argv) == 2:
        district_int = argv[1]

    filename = f"database/district_{district_int}/district-{district_int}_houses.csv"
    filename2 = f"database/district_{district_int}/district-{district_int}_batteries.csv"

    # load houses and batteries dict
    Smartgrid.houses_dict = loader.load_house(filename)
    Smartgrid.batteries_dict = loader.load_bat(filename2)

    # Create grid picture
    grid.create_grid(Smartgrid.houses_dict, Smartgrid.batteries_dict)

    # get info of case
    connections_dict = random.random_connections(Smartgrid.houses_dict, Smartgrid.batteries_dict)
    total_cost = Smartgrid.costs(Smartgrid, connections_dict, Smartgrid.batteries_dict)
    print(total_cost)
    
    #Smartgrid.output(Smartgrid, connections_dict, total_cost)
    
    # for connection in connections_dict.values:
    #     battery_x = connection.battery.x_coordinate
    #     battery_y = connection.battery.x_coordinate
    #     capacity = connection.battery.y_coordinate
    #     # houses 
    #     print("Houses information-----------------")
    #     house_x = connection.house.x_coordinate
    #     house_y = connection.house.y_coordinate
    #     print("output: ", connection.house.output)
    #     # points (x,y)


    # # print total cost
    
    # output(connections_dict, district_int, total_cost, )

