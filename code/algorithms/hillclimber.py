import copy
from hashlib import new
import random

class Hillclimber:
    """
    The HillClimber class that changes a random subset of connections to random valid new connections. Each improvement or
    equivalent solution is kept for the next iteration.
    """

    def __init__(self, smartgrid, connections_dict):
        """
        Initializes Hillclimber attributes.
        """
        self.grid = copy.deepcopy(smartgrid)
        self.connections_dict = connections_dict
        self.cost = self.grid.costs(connections_dict, self.grid.batteries_dict, shared = False)

    def remove_connections(self, part_adjust, new_connections_dict):
        """
        Removes subset of connections from connections dict.
        """
        PART_ADJUST = part_adjust

        to_connect = []

        # remove part of connections
        for i in range(PART_ADJUST):
            # make new connections_dict
            connections_list = list(new_connections_dict.keys())
            random_connection = random.choice(connections_list)
            # refill battery capacity, reset house connection
            random_pick = new_connections_dict[random_connection]
            random_pick.battery_id.output_capacity_refill(random_pick.house_id)
            random_pick.house_id.reset()

            to_connect.append(random_pick.house_id)
            # remove connection from new_connections_dict
            del(new_connections_dict[random_connection])
        
        return to_connect

    # def disconnected_houses(self):
    #     """
    #     Makes a list of houses that are not connected.
    #     """
    #     to_connect = []
    #     for house in self.houses_dict.values():
    #         if house.check_connection == False:
    #             print("False")
    #             to_connect.append(house)
    #     return to_connect

    def add_new_connections(self, new_connections_dict, to_connect):
        """
        Reconnects the disconnected houses randomly.
        """
        # list of houses to connect
        to_connect_house = to_connect               
        random.shuffle(to_connect_house)

        # fill list of batteries
        batteries_list = []
        for battery in self.grid.batteries_dict.values():
            batteries_list.append(battery)
            random.shuffle(batteries_list)
            
        # loop through houses
        for house in to_connect_house:
            print("checking house")
            if house.connected == False:
                print("house is false")
            # loop through batteries
                for battery in batteries_list:
                    print("checking a new battery")
                    print(battery.capacity)
                # connect house to battery if capacity 
                    if house.output <= battery.capacity:
                        print("there is capacity")
                        connection = self.grid.connect(battery, house)
                        # update battery capacity
                        self.grid.output_capacity(house, battery)
                        # put connection in dict
                        new_connections_dict[connection.house] = connection 

    def check_solution(self, new_connections_dict):
        """
        Compares the costs of the old and new connections.
        """
        # calculate costs of new grid
        new_costs = self.grid.costs(new_connections_dict, self.batteries_dict, shared = False)
        old_costs = self.cost
        # compare costs of old and new grids
        if new_costs <= old_costs:
            self.grid = new_connections_dict
            self.cost = new_costs
    
    def check_all_connections(self, new_connections_dict):
        """
        Returns true if all houses are connected, else is False.
        """   
        # print(len(new_connections_dict))            
        if len(new_connections_dict) == len(self.connections_dict):
            # if all houses connected
            return True    
        return False
    
    def run(self, iterations, mutate_connections_number = 5):   
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """   
        self.iterations = iterations  

        for i in range(iterations):
            
            while True:
                # Create a copy of the solution to simulate the change
                new_connections_dict = copy.deepcopy(self.connections_dict)

                # remove connections from new connections dict
                to_connect = self.remove_connections(mutate_connections_number, new_connections_dict)
                
                # add new random connections to new connections dict
                self.add_new_connections(new_connections_dict, to_connect)

                if self.check_all_connections(new_connections_dict) == True:
                    print("Check")
                    break
                else:
                    print(len(new_connections_dict))

            # Accept it if it is better
            self.check_solution(new_connections_dict)


  