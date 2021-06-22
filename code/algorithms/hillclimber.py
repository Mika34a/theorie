import copy
import random

class Hillclimber:
    """
    The HillClimber class that changes a random subset of connections 
    to random valid new connections. Each improvement or equivalent 
    solution is kept for the next iteration.
    """
    def __init__(self, smartgrid, connections_dict):
        """
        Initializes Hillclimber attributes.
        """
        self.grid = copy.deepcopy(smartgrid)
        self.connections_dict = connections_dict
        self.cost = self.grid.costs(connections_dict, self.grid.batteries_dict, shared = False)
        self.new_connections_dict = {}
        self.batteries_dict = smartgrid.batteries_dict


    def remove_connections(self, part_adjust):
        """
        Removes subset of connections from connections dict and
        returns a list of disconnected houses.
        """
        PART_ADJUST = part_adjust
        to_connect = []

        # remove part of connections
        for i in range(PART_ADJUST):
            # make new connections_dict
            connections_list = list(self.new_connections_dict.keys())
            random_connection = random.choice(connections_list)
            
            random_pick = self.new_connections_dict[random_connection]
            
            # refill battery, reset house connection
            random_pick.battery_id.output_capacity_refill(random_pick.house_id)
            random_pick.house_id.reset()

            to_connect.append(random_pick.house_id)
            
            # remove connection from new_connections_dict
            del(self.new_connections_dict[random_connection])
        
        return to_connect

    def add_new_connections(self, to_connect):
        """
        Reconnects the disconnected houses randomly.
        """
        # list of houses to connect
        to_connect_house = to_connect               
        random.shuffle(to_connect_house)

        # fill list of batteries
        batteries_list = []
        for connection in self.new_connections_dict.values():
            if connection.battery_id not in batteries_list:
                batteries_list.append(connection.battery_id)
                random.shuffle(batteries_list)
            
        # loop through houses and connect if disconnected
        for house in to_connect_house:
            for battery in batteries_list:
                
                if house.output <= battery.capacity:
                    if house.connected == False:
                        
                        connection = self.grid.connect(battery, house)
                        # update battery capacity
                        self.grid.output_capacity(house, battery)
                        # put connection in dict
                        self.new_connections_dict[connection.house] = connection

    def check_solution(self, new_connections_dict):
        """
        Compares the costs of the old and new connections
        and creates a new starting dict if the new connections
        are cheaper.
        """
        # calculate costs of new grid
        new_costs = self.grid.costs(self.new_connections_dict, self.batteries_dict, shared = False)
        old_costs = self.cost
        # compare costs of old and new grids
        if new_costs <= old_costs:
            self.connections_dict = self.new_connections_dict
            self.cost = new_costs
    
    def check_all_connections(self):
        """
        Returns True if all houses are connected, else is False.
        """
        if len(self.new_connections_dict) == len(self.connections_dict):
            return True    
        return False
    
    def run(self, iterations, mutate_connections_number = 5):   
        """
        Runs the hillclimber algorithm for a specific amount of iterations
        and returns a connections dictionary.
        """   
        self.iterations = iterations  

        for i in range(iterations):
            
            print(f'Iteration {i}/{iterations}, current value: {self.cost}') if i % 10 == 0 else None
            
            while True:
                
                # create a copy of the solution to simulate the change
                self.new_connections_dict = copy.deepcopy(self.connections_dict)  

                # remove connections from new connections dict
                to_connect = self.remove_connections(mutate_connections_number) 

                # add new random connections to new connections dict
                self.add_new_connections(to_connect)
                
                if self.check_all_connections() == True:
                    break
            
            # accept it if it is better
            self.check_solution(self.new_connections_dict)
        
        return self.connections_dict
  