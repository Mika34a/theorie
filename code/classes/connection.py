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
        self.points_list = []
        self.length = 0

    def add_point(self):
        """
        Adds a point and defines length of connection.
        """
        # loop through connections that connect to the relevant battery
        # see if points(x,y) of new connection match with one of these connections
        # len(list) = length of priced connection (first half)
        # copy/append last half of list of points to new connection

        # get coordinates from house and battery 
        house_x = self.house_id.x_coordinate
        house_y = self.house_id.y_coordinate
        battery_x = self.battery_id.x_coordinate
        battery_y = self.battery_id.y_coordinate
    	
        point_x = house_x 
        point_y = house_y
        # save the starting points
        self.points_list.append((point_x, point_y))

        # loop through all the points and append
        while True:
            if point_y < battery_y:
                point_y += 1
            elif point_y > battery_y:
                point_y -= 1
            elif point_x < battery_x:
                point_x += 1
            elif point_x > battery_x:
                point_x -= 1        
            else:
                break
            self.points_list.append((point_x, point_y))
        self.length = (abs(battery_x - house_x)) + (abs(battery_y - house_y))    
                
    
            
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
        Returns house id of connection
        """
        return self.house_id.id

    def battery(self):
        """
        Returns battery id of connection
        """   
        return self.battery_id.id
    
    def bat_y_coordinate(self):
        return self.battery_id.y_coordinate     

    def bat_x_coordinate(self):
        return self.battery_id.x_coordinate
    
    def start_capacity(self):
        return self.battery_id.start_capacity
    
    def house_x_coordinate(self):
        return self.house_id.x_coordinate

    def house_y_coordinate(self):
        return self.house_id.y_coordinate

    def output(self):
        return self.house_id.output

    def points_list(self):
        return self.points_list
        
            

