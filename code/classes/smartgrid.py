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
import time
from code.classes import loader

class Smartgrid():
    def __init__(self, filename, filename2):
        """
        Initializes the Smartgrid class.
        """
        self.houses_dict= loader.load_house(filename)
        self.batteries_dict = loader.load_batteries(filename2) 

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
        
    def output(self, connections_dict, total_cost, runtime, main):
        """
        Prints output information about solution.
        """
        with open('output/output_random.txt', 'w') as f:
            f.write(
            f'''
            Case information-------------------------
            Runtime: {runtime} seconds
            District {main}
            Shared costs: {total_cost}
            ''')
            
            for battery in self.batteries_dict.values():
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

    def match_point(self):
        # loop door connecties (def geselecteerde connectie)
        for connection in self.connections_dict.values():
        # wat is de batterij? 
            battery = connection.battery
            # loop connecties zonder geselecteerde connectie 
            for connection2 in self.connections_dict.values():
                if connection is not connection2 and connection.battery is connection2.battery:
                    for point in connection.points_list:
                        for point2 in connection2.points_list:
                            if point == point2:
                                return True


            # if batterij is zelfde
            # loop door points of geselecteerde connectie
            # loop door points other conneciton
                # als punten matchen: return True (length is dan gelijk aan lengte over y as)

                #hij loop eerst door Y coordinaten en dan door x coordinaten

        for 

        for connection in self.connections_dict.values():
            if connection.battery == battery:
                for match in connection.points_list:
                    if match == point:
                        return True

    
