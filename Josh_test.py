from code.classes import loader
from code.grid import grid

houses_dict = loader.load_house()
batteries_dict = loader.load_bat()

grid.create_grid(houses_dict, batteries_dict)

