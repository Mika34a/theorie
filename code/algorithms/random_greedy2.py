class RandomGreedy(Random):
    """
    The Greedy class that connects the best possible battery to each house one by one.
    """
    def __init__():
        pass
    def close_batteries(house):
        batteries_closest = Random.grid.proximity(house, Random.grid.batteries_dict)
        return batteries_closest  

    def connect_greedy(self, house, close_batteries):
        for battery in close_batteries:
            if  house.output <= battery.capacity:
                # check if house is already connected
                if house.connected == False:
                    connection = Random.grid.connect(battery, house)

                    # update battery capacity
                    Random.grid.output_capacity(house, battery)

                    # put connection in dict
                    Random.connections_dict[connection.house] = connection      

    def run(self):
        while True:
            Random.randomize_houses()
            for house in Random.houses_list:
                close_batteries = self.close_batteries(house)
                connections_dict = self.connect_greedy(house, close_batteries)
                if self.check_all_connections(connections_dict) == False:
                    continue
                else:
                    return connections_dict 





