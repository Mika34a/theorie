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
import time

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
        
    def output(self, connections_dict, total_cost, runtime):
        """
        Prints output information about solution.
        """
        with open('output.txt', 'w') as f:
            f.write(
            f'''
            Case information-------------------------
            Runtime: {runtime} seconds
            District {argv[1]}
            Shared costs: {total_cost}
            ''')
            
            for battery in Smartgrid.batteries_dict.values():
                f.write(
                f'''
                Battery ------------------------
                Location: {battery.x_coordinate}, {battery.y_coordinate}
                Capacity: {battery.start_capacity}
                ''')
                for connection in connections_dict.values():
                    if connection.battery() == battery.id:
                        f.write(
                            f'''
                            Location: {connection.house_x_coordinate()}, {connection.house_y_coordinate()}
                            Output: {connection.output()}
                            Connection points: {connection.points_list}
                            '''
                            )
            f.close()

    def all_connected(self, houses_list, connections_dict):
        if len(connections_dict) == len(houses_list):
            return True
        return False  

runtime = time.time()

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
    connections_dict = random.run(Smartgrid.houses_dict, Smartgrid.batteries_dict)
    total_cost = Smartgrid.costs(Smartgrid, connections_dict, Smartgrid.batteries_dict)
    print(total_cost)
    for connection in connections_dict.values():
        print(connection.points_list)
    
    
    # export output to txt file
    Smartgrid.output(Smartgrid, connections_dict, total_cost, (time.time()-runtime))
    

