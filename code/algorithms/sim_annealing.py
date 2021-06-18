# sim_annealing.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements a simulated annealing algorithm to connect houses to batteries
# - connections are shared between houses if more efficient.
# - with the algorithm preferencing the batteries that are closest by first.

import random
import math

def run(smartgrid, connections_dict):
    # Choose a random start state
    start_state = connections_dict
    
    # Choose starting temperature
    start_T = 285
    final_T = .1
    T = start_T
    cooling = 1
    chance = 0.2
    
    # Repeat N times
    while T > final_T:
        # smaller random adjustment
        new_state = smartgrid.random_adjust(start_state)
        cost_diff = smartgrid.costs(start_state) - smartgrid.costs(new_state)
        
        if cost_diff > 0:
            start_state = new_state
        else:
            # If random()<chance(old, new, temp):
            if random.random() < math.exp(cost_diff / T):
                start_state = new_state
        # decrease temperature        
        T -= cooling

    return new_state