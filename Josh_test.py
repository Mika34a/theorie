from code.classes.smartgrid import Smartgrid
from code.classes import loader
from code.grid import grid
from code.algorithms import random
from sys import argv
import time

# # check command line
# if len(argv) != 2:
#     print("Usage: python3 smartgrid.py [district_number]")
#     exit(1)
# # Load the requested files
# if len(argv) == 2:
#     district_int = argv[1]

# filename = f"database/district_{district_int}/district-{district_int}_houses.csv"
# filename2 = f"database/district_{district_int}/district-{district_int}_batteries.csv"

# print(filename)
# print(filename2)

# houses_dict = loader.load_house(filename)
# batteries_dict = loader.load_bat(filename2)

# grid.create_grid(houses_dict, batteries_dict)

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

    # Create grid picture
    grid.create_grid(smartgrid.houses_dict, smartgrid.batteries_dict)

    # get info of case
    connections_dict = random.run(smartgrid)
    total_cost = smartgrid.costs(connections_dict, smartgrid.batteries_dict)
    print(total_cost)
    # for connection in connections_dict.values():
    #     print(connection.points_list)
    
    
    # export output to txt file
    smartgrid.output(connections_dict, total_cost, (time.time()-runtime), argv[1])