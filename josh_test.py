from code.classes.smartgrid import Smartgrid
from code.classes import loader
from code.algorithms.hillclimber import Hillclimber
from code.algorithms.sim_annealing import SimulatedAnnealing
from code.grid import grid
from code.algorithms import greedy_random, random, greedy_random_shared, sim_annealing, hillclimber
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

    filename = f"database/district_{district_int}/district-{district_int}_houses.csv"
    filename2 = f"database/district_{district_int}/district-{district_int}_batteries.csv"

    # load houses and batteries dict
    smartgrid = Smartgrid(filename, filename2)

    # get info of case
    all_costs = []
    all_runtimes = []
    N = 1

    for n in range(N):                                                                                                                                                                                     
        connections_dict = greedy_random.run(smartgrid)
        climber = Hillclimber(smartgrid, connections_dict)
        final_connections_dict = climber.run(100)
        # s_annealing = SimulatedAnnealing(smartgrid, connections_dict)
        # final_connections_dict = s_annealing.run(100)
        total_cost = smartgrid.costs(final_connections_dict, smartgrid.batteries_dict, shared)
        print(total_cost)
        print(time.time()-runtime)
        all_costs.append(total_cost)
        all_runtimes.append(time.time()-runtime)

    # average_costs  = sum(all_costs) / N
    # average_runtime = sum(all_runtimes) / N
    # print(average_costs, statistics.stdev(all_costs))

    # Create grid picture
    grid.create_grid    (smartgrid.houses_dict, smartgrid.batteries_dict, final_connections_dict)
    # print(total_cost)
    # for connection in connections_dict.values():
    #     print(connection.points_list)
    
    # export output to json file
    smartgrid.output(final_connections_dict, total_cost, (time.time()-runtime), argv[1], shared = False)