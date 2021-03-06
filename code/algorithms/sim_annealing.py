# sim_annealing.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements a simulated annealing algorithm to connect houses to batteries 
#   within capacity.


import random
import numpy as np
from .hillclimber import Hillclimber

class SimulatedAnnealing(Hillclimber):
    """
    The SimulatedAnnealing class that changes random connections in the grid.
    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.
    """
    def __init__(self, smartgrid, connections_dict, temp=501):
        """
        Initialises the Simulated Annealing.
        """
        super().__init__(smartgrid, connections_dict)

        self.T0 = temp
        self.T = temp

    def update_temp(self):
        """
        Linear cooling scheme, with temperature becoming zero
        after all iterations.
        """
        self.T = self.T - (self.T0 / self.iterations)

    def check_solution(self, new_connections_dict):
        """
        Compares the costs of the old and new connections.
        """
        # calculate costs of new grid
        new_costs = self.grid.costs(new_connections_dict, self.batteries_dict, shared = False)
        old_costs = self.cost
        
        costdif = new_costs - old_costs
        chance = np.exp(-costdif / self.T)

        if random.random() < chance:
            self.connections_dict = new_connections_dict
            self.cost = new_costs

        self.update_temp()
