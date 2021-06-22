# connection.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements Connection class.

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
        self.points_x = []
        self.points_y = []


    def add_point(self):
        """
        Adds a point and defines length of connection.
        """
        # get coordinates from house and battery 
        house_x = self.house_id.x_coordinate
        house_y = self.house_id.y_coordinate
        battery_x = self.battery_id.x_coordinate
        battery_y = self.battery_id.y_coordinate
    	
        point_x = house_x 
        point_y = house_y
        
        # save the starting points
        self.points_list.append((point_x, point_y))
        self.points_x.append(point_x)
        self.points_y.append(point_y)

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
            self.points_x.append(point_x)
            self.points_y.append(point_y)
        
        # Manhattan distance, with +1 because of ending location
        self.length = (abs(battery_x - house_x)) + (abs(battery_y - house_y)) + 1

    def length(self):
        """
        Returns length of connection.
        """
        return self.length

    def house(self):
        """
        Returns house id of connection.
        """
        return self.house_id.id

    def battery(self):
        """
        Returns battery id of connection. 
        """   
        return self.battery_id.id
    
    def house_x_coordinate(self):
        """
        Returns x coordinate from house that belongs to connection.
        """  
        return self.house_id.x_coordinate

    def house_y_coordinate(self):
        """
        Returns y coordinate from house that belongs to connection.
        """  
        return self.house_id.y_coordinate

    def output(self):
        """
        Returns output from house that belongs to connection.
        """  
        return self.house_id.output

    def __repr__(self) -> str:
        """
        Representation of connection.
        """  
        return f"{self.points_list}"
        
            

