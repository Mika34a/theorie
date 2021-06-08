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
        self.house_id = house
        self.battery_id = battery 
        self.points_x = []
        self.points_y = []
        self.length = 0

    def add_point(self):
        """
        Adds a point and defines length of connection.
        """
        # get coordinates from house and battery 
        house_x = self.house_id.x_coordinate
        house_y = self.house_id.y_coordinate
        battery_x = self.battery_id.x_coordinate
        battery_y = self.battery_id.y_coordinate

        # find manhatten distance
        vector = (abs(battery_x - house_x)) + (abs(battery_y - house_y))
        x_vector = abs(battery_x - house_x) 
        y_vector = abs(battery_y - house_y)

        # append x segments passed between a and b to list 
        for point_x in range (battery_x, house_x, 1):
            self.points_x.append(point_x)
        
        # append y segments passed between a and b to list 
        for point_y in range (battery_y, house_y, 1):
            self.points_y.append(point_y)
        # Set length for connection (Manhatten distance)
        self.length = vector

        # put points between x and y in list
        points_list = zip(self.points_x, self.points_y)   


# functions
    def return_points(self): 
        """
        Returns all points of the grid that the connection crosses.
        """
        return self.return_points

    def length(self):
        """
        Returns length of connection.
        """
        return self.length

    def house(self):
        """
        Returns house of connection
        """
        return self.house_id

    def battery(self):
        """
        Returns battery of connection
        """   
        return self.battery_id

        
            

