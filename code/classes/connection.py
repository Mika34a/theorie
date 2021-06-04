# connection.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements Connection class.

# class Connections
class Connection:
    def __init__(self, house, battery):
        """
        Initializes Connection class.
        """
        # attributes 
        self.house = house
        self.battery = battery 
        self.points_x = []
        self.points_y = []

    def add_point(self):
        """
        Adds a point.
        """
        # get coordinates from house and battery 
        house_x = self.house.x_coordinate
        house_y = self.house.y_coordinate
        battery_x = self.battery.x_coordinate
        battery_y = self.battery.y_coordinate

        # find manhatten distance
        vector = (abs(battery_x - house_x)) + (abs(battery_y - house_y))
        x_vector = abs(battery_x - house_x) 
        y_vector = abs(battery_y - house_y)
       
        # put points between x and y in list

        # append x segments passed between a and b to list 
        for point_x in range (battery_x, house_x, 1):
            self.points_x.append(point_x)
        
        # append y segments passed between a and b to list 
        for point_y in range (battery_y, house_y, 1):
            self.points_y.append(point_y)
            

