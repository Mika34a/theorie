# smartgrid.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements smartgrid class.

# from .connection import Connection
# from .house import House
# from .loader import *

from code.classes import *
from code.classes.connection import Connection
from code.classes.house import House
from code.classes.battery import Battery
from code.algorithms import random

class Smartgrid():

    # functions
    # - connect batteries with houses 
    # - return total costs of connections and batteries 
    # - return houses if not connected
    # - return batteries with capacity left

    def __init__(self, filename, filename2):
        """
        Initializes the Smartgrid class.
        """
        self.houses_dict= self.loader.load_house(filename)
        self.batteries_dict = self.loader.load_batteries(filename2) 

    def connect(self, battery, house):
        connection = Connection(house, battery)
        connection.add_point()
        print(connection.length)
        return connection

    def costs(self, connections_dict):
        """
        Returns the total costs of the combined cables.
        """
        # laying a cable costs 9 per grid
        # costs for each battery is 5000, with each district having 5 batteries
        COST_GRID = 9
        COST_BATTERY = 5000
        COST_CABLE_ALL = 0

        for con in connections_dict.values():
            COST_CABLE = con.length * COST_GRID

            COST_CABLE_ALL = COST_CABLE_ALL + COST_CABLE


        return COST_CABLE_ALL

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

    # print(filename)
    # print(filename2)

    # load houses and batteries dict
    Smartgrid.houses_dict = loader.load_house(filename)
    Smartgrid.batteries_dict = loader.load_bat(filename2)

    # Create grid picture
    grid.create_grid(Smartgrid.houses_dict, Smartgrid.batteries_dict)

    # print total cost
    connections_dict = random.random_connections(Smartgrid.houses_dict, Smartgrid.batteries_dict)
    total_cost = Smartgrid.costs(Smartgrid, connections_dict)
    print(total_cost)

