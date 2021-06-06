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
        return connection

    def costs(self, connection):
        """
        Returns the total costs of the combined cables.
        """
        # laying a cable costs 9 per grid
        # costs for each battery is 5000, with each district having 5 batteries
        cost_grid = 9
        cost_battery = 5000
        cost_cable_all = 0

        for c in connection:
            cost_cable = connection.length * cost_grid

            cost_cable_all = cost_cable_all + cost_cable


        return cost_cable_all
        

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

    print(Smartgrid.houses_dict)