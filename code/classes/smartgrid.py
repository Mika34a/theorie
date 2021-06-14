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
import json

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
        
    # def output(self, connections_dict, total_cost, runtime, main):
    #     total_list = [
    #         {
    #             "district": int(main),
    #             "own-costs": total_cost,
    #         },         
    #         {
    #             "location": str({battery.x_coordinate}, {battery.y_coordinate}),
    #             "capacity": str({battery.start_capacity}),
    #             "houses": [                       
    #                         {
    #                             "location": str({connection.house_x_coordinate()}, {connection.house_y_coordinate()}),
    #                             "output": str({connection.output()}),
    #                             "cables": [str({point}) for point in connection.points_list]
    #                         }
    #             for connection in connections_dict.values() if connection.battery() == battery.id]
    #         for battery in self.batteries_dict.values()} 
    #     ] 

    # # the json file where the output must be stored
    # out_file = open("random_output.json", "w")
    
    # json.dump(total_list, out_file, indent = 1)
    
    # out_file.close()

            
    
    def output(self, connections_dict, total_cost, runtime, main):
        """
        Prints output information about solution.
        """
        with open('output/output_random.json', 'w') as f:
            f.write(
            f'''
            Runtime: {runtime} seconds
            District {main}
            Own-costs: {total_cost}
            ''')
            
            for battery in self.batteries_dict.values():
                f.write(
                f'''
                location: {battery.x_coordinate}, {battery.y_coordinate}
                capacity: {battery.start_capacity}
                ''')
                for connection in connections_dict.values():
                    if connection.battery() == battery.id:
                        f.write(
                            f'''
                            location: {connection.house_x_coordinate()}, {connection.house_y_coordinate()}
                            output: {connection.output()}
                            connection points: {connection.points_list}
                            '''
                            )
            f.close()

    def all_connected(self, houses_list, connections_dict):
        if len(connections_dict) == len(houses_list):
            return True
        return False  
