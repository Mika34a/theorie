# random.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements a random algorithm to connect houses to batteries 
#   within capacity.

import random

class Random:
    """
    The Random class that connects a random best possible battery to random houses one by one.
    """
    def __init__(self, smartgrid):
        self.batteries_dict = smartgrid.batteries_dict
        self.houses_dict = smartgrid.houses_dict
        self.grid = smartgrid
        self.connections_dict = {}
        self.houses_list = []
        self.batteries_list = []

    def randomise_houses(self):
        """"
        Randomises the list of houses.
        """
        for house in self.houses_dict.values():
            self.houses_list.append(house)
        random.shuffle(self.houses_list) 

    def randomise_batteries(self):
        """"
        Randomises the list of batteries.
        """
        for battery in self.batteries_dict.values():
            self.batteries_list.append(battery)
        random.shuffle(self.batteries_list)         

    def connect_houses(self):
        """"
        Connects the houses to the batteries randomly.
        """
        for house in self.houses_list:    
            # check if output of house still fits in capacity battery 
            for battery in self.batteries_list:
                
                # connect house to battery 
                if  house.output <= battery.capacity:
                    
                    # check if house is already connected
                    if house.connected == False:
                        connection = self.grid.connect(battery, house)

                        # update battery capacity
                        self.grid.output_capacity(house, battery)

                        # put connection in dict
                        self.connections_dict[connection.house] = connection                  
    
    def check_all_connections(self, connections_dict):
        """"
        Checks if all houses are connected. If not, resets all houses and batteries.
        """ 
        # if all houses connected              
        if self.grid.all_connected(connections_dict):
            return True
        # reset is not all connected
        else:
            for battery in self.batteries_dict.values():
                battery.reset()
            for house in self.houses_dict.values():
                house.reset()
            return False                          

    def run(self):
        """"
        Runs the Random algorithm.
        """
        # run until all houses are connected
        while True:
            self.randomise_houses()
            self.randomise_batteries()
            self.connect_houses()

            # if all houses are connected
            if self.check_all_connections(self.connections_dict):
                return self.connections_dict   
            # reset connections dict if not all houses are connected
            else:
                self.connections_dict = {}       

