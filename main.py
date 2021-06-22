# main.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements several algorithms to connect houses to batteries with capacity. 

from code.algorithms.random_greedy import RandomGreedy
from code.classes.smartgrid import Smartgrid
from code.algorithms.hillclimber import Hillclimber
from code.algorithms.sim_annealing import SimulatedAnnealing
from code.algorithms.random import Random
from code.grid import grid
from sys import argv
import time
import statistics

runtime = time.time()

if __name__ == "__main__":

    # check command line
    if len(argv) != 4:
        print("Usage: python3 smartgrid.py [district_number] random/greedy/climber/sim shared:y/n")
        exit(1)
    # Load the requested files
    if len(argv) == 4:
        district_int = argv[1]
        shared = argv[3]
        algorithm = argv[2]

        if argv[3] == "shared:y":
            shared = True
        elif argv[3] == "shared:n":
            shared = False
        else:
            print("Usage: python3 smartgrid.py [district_number] random/greedy/climber/sim shared:y/n")

    housesf = f"database/district_{district_int}/district-{district_int}_houses.csv"
    batteriesf = f"database/district_{district_int}/district-{district_int}_batteries.csv"

    # load houses and batteries dict
    smartgrid = Smartgrid(housesf, batteriesf)

    # get info of case
    all_costs = []
    all_runtimes = []
    N = 5
    IT = 100

    for n in range(N):
    #------------------------------random algorithm-------------------------------
        if algorithm == "random":
            random_a = Random(smartgrid)
            final_connections_dict = random_a.run()

    #---------------------------random greedy algorithm---------------------------
        elif algorithm == "greedy":
            randomgreedy_a = RandomGreedy(smartgrid)
            final_connections_dict = randomgreedy_a.run()

    #----------------------------hillclimber algorithm----------------------------
        elif algorithm == "climber":
            randomgreedy_a = RandomGreedy(smartgrid)
            connections_dict = randomgreedy_a.run()
            climber = Hillclimber(smartgrid, connections_dict)
            final_connections_dict = climber.run(IT)

    # -----------------------------simulated annealing-----------------------------
        elif algorithm == "sim":
            randomgreedy_a = RandomGreedy(smartgrid)
            connections_dict = randomgreedy_a.run()
            s_annealing = SimulatedAnnealing(smartgrid, connections_dict)
            final_connections_dict = s_annealing.run(IT)

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
smartgrid.output(final_connections_dict, total_cost, (time.time()-runtime), argv[1], shared)