# main.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements several algorithms to connect houses to batteries with capacity. 
# - Comment out algorithms that you don't wish to use.
# - Use one algorithm at a time.

from code.classes.smartgrid import Smartgrid
from code.algorithms.hillclimber import Hillclimber
from code.algorithms.sim_annealing import SimulatedAnnealing
from code.algorithms.random2 import Random
# from code.algorithms.random_greedy2 import RandomGreedy
from code.grid import grid
from code.algorithms import greedy_random, random
from sys import argv
import time
import statistics

runtime = time.time()

if __name__ == "__main__":

    # check command line
    if len(argv) != 3:
        print("Usage: python3 smartgrid.py [district_number] shared:y/n")
        exit(1)
    # Load the requested files
    if len(argv) == 3:
        district_int = argv[1]
        shared = argv[2]
        if argv[2] == "shared:y":
            shared = True
        elif argv[2] == "shared:n":
            shared = False
        else:
            print("Usage: python3 smartgrid.py [district_number] shared:y/n")

    housesf = f"database/district_{district_int}/district-{district_int}_houses.csv"
    batteriesf = f"database/district_{district_int}/district-{district_int}_batteries.csv"

    # load houses and batteries dict
    smartgrid = Smartgrid(housesf, batteriesf)

    # get info of case
    all_costs = []
    all_runtimes = []
    N = 5

    for n in range(N):
    #------------------------------random algorithm-------------------------------
        random_a = Random(smartgrid)
        final_connections_dict = random_a.run()

    #---------------------------random greedy algorithm---------------------------
        # final_connections_dict = greedy_random.run(smartgrid)

    #----------------------------hillclimber algorithm----------------------------
        # connections_dict = greedy_random.run(smartgrid)
        # climber = Hillclimber(smartgrid, connections_dict)
        # final_connections_dict = climber.run(100)

    # -----------------------------simulated annealing-----------------------------
        # connections_dict = greedy_random.run(smartgrid)
        # s_annealing = SimulatedAnnealing(smartgrid, connections_dict)
        # final_connections_dict = s_annealing.run(3000)

        total_cost = smartgrid.costs(final_connections_dict, smartgrid.batteries_dict, shared)
        print(total_cost)
        print(time.time()-runtime)
        all_costs.append(total_cost)
        all_runtimes.append(time.time()-runtime)
    
    average_costs  = sum(all_costs) / N
    average_runtime = sum(all_runtimes) / N
    print(average_costs, statistics.stdev(all_costs))

# compute costs
total_cost = smartgrid.costs(final_connections_dict, smartgrid.batteries_dict, shared)
# create grid picture
grid.create_grid(smartgrid.houses_dict, smartgrid.batteries_dict, final_connections_dict)
# export output to json file
smartgrid.output(final_connections_dict, total_cost, (time.time()-runtime), argv[1], shared = True)