from code.classes.smartgrid import Smartgrid
from code.classes import loader
from code.grid import grid
from code.algorithms import greedy_random_shared, random
from code.algorithms import greedy_random as greedy
from sys import argv
import statistics
import time

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

    N = 30
    cheapest = 100000
    total = []

    for n in range(N):
        # load houses and batteries dict
        smartgrid = Smartgrid(filename, filename2)

        # get info of case
        connections_dict = greedy.run(smartgrid)
        new_cost = smartgrid.costs(connections_dict, smartgrid.batteries_dict)

        # save results if current run is the cheapest
        if new_cost < cheapest:
            cheapest = new_cost

            # export output to txt file
            smartgrid.output_greedy(connections_dict, cheapest, (time.time()-runtime), argv[1])

            # Create grid picture
            grid.create_grid(smartgrid.houses_dict, smartgrid.batteries_dict, connections_dict)

        total.append(new_cost)
    
    average_cost = sum(total) / N
        
    print(cheapest)
    print(statistics.stdev(total))
    print(average_cost)

    