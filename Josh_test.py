from code.classes import loader
from code.grid import grid
from sys import argv

# check command line
if len(argv) != 2:
    print("Usage: python3 smartgrid.py [district_number]")
    exit(1)
# Load the requested files
if len(argv) == 2:
    district_int = argv[1]

filename = f"database/district_{district_int}/district-{district_int}_houses.csv"
filename2 = f"database/district_{district_int}/district-{district_int}_batteries.csv"

print(filename)
print(filename2)

houses_dict = loader.load_house(filename)
batteries_dict = loader.load_bat(filename2)

grid.create_grid(houses_dict, batteries_dict)
