
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
        self.batteries_list= []

    def randomise_houses(self):
        for house in self.houses_dict.values():
            self.houses_list.append(house)
        random.shuffle(self.houses_list) 

    def randomise_batteries(self):
        for battery in self.batteries_dict.values():
            self.batteries_list.append(battery)
        random.shuffle(self.batteries_list)         


    def connect_houses(self):
        connections_dict = {}
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
                        connections_dict[connection.house] = connection   
        return connections_dict                 
    
    def check_all_connections(self, connections_dict): 
        # all_connected               
        if self.grid.all_connected(connections_dict):
            return True
        else:
            for battery in self.batteries_list:
                battery.reset()
            for house in self.houses_list:
                house.reset()
            return False                          

    def run(self):
        while True:
            self.randomise_houses()
            self.randomise_batteries()
            connections_dict = self.connect_houses()
            if self.check_all_connections(connections_dict) == False:
                continue     
            else:
                return connections_dict    

