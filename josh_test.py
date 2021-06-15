from code.classes.smartgrid import Smartgrid
from code.classes import loader
from code.grid import grid
from code.algorithms import greedy_random, random, greedy_random_shared
from sys import argv
import time
import statistics

runtime = time.time()

if __name__ == "__main__":

    # check command line
    if len(argv) != 2:
        print("Usage: python3 smartgrid.py [district_number]")
        exit(1)
    # Load the requested files
    if len(argv) == 2:
        district_int = argv[1]

    filename = f"database/district_{district_int}/district-{district_int}_houses.csv"
    filename2 = f"database/district_{district_int}/district-{district_int}_batteries.csv"

    # load houses and batteries dict
    smartgrid = Smartgrid(filename, filename2)

    # get info of case
    all_costs = []
    all_runtimes = []
    N = 1000

    for n in range(N):
        connections_dict = random.run(smartgrid)
        total_cost = smartgrid.costs(connections_dict, smartgrid.batteries_dict)
        # print(total_cost)
        # print(time.time()-runtime)
        all_costs.append(total_cost)
        # all_runtimes.append(time.time()-runtime)

    average_costs  = sum(all_costs) / N
    # average_runtime = sum(all_runtimes) / N
    print(average_costs, statistics.stdev(all_costs))

    # Create grid picture
    grid.create_grid(smartgrid.houses_dict, smartgrid.batteries_dict, connections_dict)
    # print(total_cost)
    # for connection in connections_dict.values():
    #     print(connection.points_list)
    
    # export output to txt file
    smartgrid.output(connections_dict, total_cost, (time.time()-runtime), argv[1])