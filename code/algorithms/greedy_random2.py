
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

    def randomize_houses(self):
        for house in self.houses_dict.values():
            self.houses_list.append(house)
            random.shuffle(self.houses_list) 

    def randomize_batteries(self):
        for battery in self.batteries_dict.values():
            self.batteries_list.append(battery)
            random.shuffle(self.batteries_list)         


    def connect_houses(self):
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
    
    def check_all_connections(self): 
        # all_connected                
        if self.grid.all_connected(self.connections_dict):
            return self.connections_dict
        else:
            for battery in self.batteries_list:
                battery.reset()
            for house in self.houses_list:
                house.reset()
            False                          

    def run(self):
        while True:
            self.randomize_houses()
            self.randomize_batteries()
            self.connect_houses()
            if self.check_all_connections() == False:
                continue


class RandomGreedy(Random):
    """
    The Greedy class that connects the best possible battery to each house one by one.
    """
    def close_batteries(Random, house):
        batteries_closest = Random.grid.proximity(house, Random.grid.batteries_dict)
        return batteries_closest  

    def connect_greedy(self, house, close_batteries):
        for battery in close_batteries:
            if  house.output <= battery.capacity:
                # check if house is already connected
                if house.connected == False:
                    connection = Random.grid.connect(battery, house)

                    # update battery capacity
                    Random.grid.output_capacity(house, battery)

                    # put connection in dict
                    Random.connections_dict[connection.house] = connection      

    def run(self):
        while True:
            random.randomize_houses()
            for house in Random.houses_list:
                close_batteries = self.close_batteries(house)
                self.connect_greedy(house, close_batteries)
                if self.check_all_connections() == False:
                    continue





