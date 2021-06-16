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

    def costs(self, connections_dict, battery_dict, shared):
        """
        Returns the total costs of the combined cables.
        """
        # laying a cable costs 9 per grid
        # costs for each battery is 5000
        COST_GRID = 9
        COST_BATTERY = 5000
        cost_cable_all = 0

        if shared == False: 
            for con in connections_dict.values():
                cost_cable = con.length * COST_GRID
                cost_cable_all = cost_cable_all + cost_cable

        else:
            amount_segments_total = 0

            #for every battery
            for battery in self.batteries_dict.values():
                # make empty set
                set_coordinates = set() 
                # for every connection with same battery
                for con in connections_dict.values():
                    if con.battery_id == battery:
                        # loop through points_list and add to set
                        for coordinate in con.points_list:
                            set_coordinates.add(coordinate)       
                amount_segments_battery = len(set_coordinates)
                amount_segments_total = amount_segments_battery + amount_segments_total
                print(amount_segments_total)
            cost_cable_all = COST_GRID * amount_segments_total

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
        Gives the output of the algorithm in json format.
        """
        total_list = []

        total_list.append({"district": int(main), "costs-shared": (total_cost)})

        for battery in self.batteries_dict.values():
            houses = []
            total_list.append({"location": f"{battery.x_coordinate},{battery.y_coordinate}", "capacity": battery.start_capacity, "houses": houses })
            
            for connection in connections_dict.values():
                if connection.battery() == battery.id:
                    cables = []
                    for point in connection.points_list:
                        x,y = point
                        cables.append(f"{x},{y}")

                    houses.append({"location": f"{connection.house_x_coordinate()},{connection.house_y_coordinate()}", "output": connection.output(), "cables": cables})

        # the json file where the output must be stored
        out_file = open("output.json", "w")
               
        json.dump(total_list, out_file, indent = 2)
        
        out_file.close()

    def output_greedy(self, connections_dict, total_cost, runtime, main):
        """
        Prints output information about solution.
        """
        total_list = []

        total_list.append({"district": int(main), "costs-shared": (total_cost)})

        for battery in self.batteries_dict.values():
            houses = []
            total_list.append({"location": f"{battery.x_coordinate},{battery.y_coordinate}", "capacity": battery.start_capacity, "houses": houses })
            
            for connection in connections_dict.values():
                if connection.battery() == battery.id:
                    cables = []
                    for point in connection.points_list:
                        x,y = point
                        cables.append(f"{x},{y}")

                    houses.append({"location": f"{connection.house_x_coordinate()},{connection.house_y_coordinate()}", "output": connection.output(), "cables": cables})

        # the json file where the output must be stored
        out_file = open("output.json", "w")
               
        json.dump(total_list, out_file, indent = 2)
        
        out_file.close()

    def all_connected(self, houses_list, connections_dict):
        if len(connections_dict) == len(houses_list):
            return True
        return False  

    def proximity(self, house, batteries_dict):
        """
        Takes a house and the dictionary of batteries and generates a dictionary
        of batteries in ascending order of the distance between house and battery.
        """        
        distances = {}

        for battery in batteries_dict.values():
            
            distance = (abs(battery.x_coordinate - house.x_coordinate)) + (abs(battery.y_coordinate - house.y_coordinate))
            
            distances[battery] = distance

        # sort batteries ascending by distance value 
        sorted_batteries = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
        return sorted_batteries

    def distance(self, x, y, house):
        """
        Returns manhatten distance between a coordinate and a house.
        """   
        distance = (abs(x - house.x_coordinate)) + (abs(y - house.y_coordinate))   
        return distance

    def near_connection(self, house, battery, connections_dict):
        """
        Loops through coordinates of all connections for a battery and calculates distance to house. 
        Returns coordinate with smallest distance to house.
        """     
        count = 0
        minimum = False
        # loop through connections
        for connection in connections_dict.values():    
            # if battery is battery
            if connection.battery_id == battery:
                # loop through points_list
                for coordinate in connection.points_list:
                    # check distance for connection.points_list
                    x = coordinate[0]
                    y = coordinate[1]

                    distance = (abs(x- house.x_coordinate)) + (abs(y - house.y_coordinate))
                    if count == 0:
                        minimum = coordinate
                        minimum_dist = distance
                        count += 1
                    else:
                        if distance < minimum_dist:
                            minimum = coordinate                     
        return minimum 

    
