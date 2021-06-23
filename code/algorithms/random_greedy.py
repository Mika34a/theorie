# random_greedy.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements a random greedy algorithm to connect houses to batteries 
#   within capacity.
# - Chooses the closest battery possible for every house.

from .random import Random

class RandomGreedy(Random):
    """
    The Random Greedy class that connects the best possible battery to each house one by one.
    """
    def __init__(self, smartgrid):
        """
        Initialises RandomGreedy attributes.
        """
        Random.__init__(self, smartgrid)

    def close_batteries(self, house):
        """
        Returns closest batteries.
        """
        batteries_closest = self.grid.proximity(house, self.grid.batteries_dict)
        return batteries_closest  

    def connect_greedy(self):
        """
        Connects houses to batteries based on proximity.
        """
        for house in self.houses_list:
            close_batteries = self.close_batteries(house)
            for battery in close_batteries:
                
                if house.output <= battery.capacity:
                    
                    # check if house is already connected
                    if house.connected == False:
                        connection = self.grid.connect(battery, house)

                        # update battery capacity
                        self.grid.output_capacity(house, battery)

                        # put connection in dict
                        self.connections_dict[connection.house] = connection
                             
    def run(self):
        """
        Runs Random Greedy algorithm.
        """
        # run until all houses are connected
        while True:
            self.randomise_houses()
            self.connect_greedy()

            # if all houses are connected
            if self.check_all_connections(self.connections_dict):
                return self.connections_dict    
            # reset connections dict if not all houses are connected
            else:
                self.connections_dict = {}     

                 





