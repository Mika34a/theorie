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
        # get coordinates from house and battery 
        house_x = self.house_id.x_coordinate
        house_y = self.house_id.y_coordinate
        battery_x = self.battery_id.x_coordinate
        battery_y = self.battery_id.y_coordinate

        if house_y > battery_y:
            for point_y in range(house_y, (battery_y - 1), -1):
                if house_x > battery_x:
                    for point_x in range(house_x, (battery_x - 1), -1):
                           self.points_list.append((point_x, point_y))
                elif house_x < battery_x:
                    for point_x in range(house_x, (battery_x + 1), 1):
                        self.points_list.append((point_x, point_y))
                else:
                    point_x = house_x
                    self.points_list.append((point_x, point_y))
        elif house_y < battery_y:
            for point_y in range(house_y, (battery_y + 1), 1):
                if house_x > battery_x:
                    for point_x in range(house_x, (battery_x - 1), -1):
                        self.points_list.append((point_x, point_y))
                elif house_x < battery_x:
                    for point_x in range(house_x, (battery_x + 1), 1):
                        self.points_list.append((point_x, point_y))
                else:
                    point_x = house_x 
                    self.points_list.append((point_x, point_y))                     
        else:
            point_y = house_y 
            if house_x > battery_x:
                for point_x in range(house_x, (battery_x - 1), -1):
                    self.points_list.append((point_x, point_y))
            elif house_x < battery_x:
                for point_x in range(house_x, (battery_x + 1), 1):
                    self.points_list.append((point_x, point_y))
            else:
                point_x = house_x
                self.points_list.append((point_x, point_y))

        # find manhatten distance
        self.length = (abs(battery_x - house_x)) + (abs(battery_y - house_y))

        # append x & y segments passed between a and b to list
        # for point_y in range (house_y, (battery_y + 1)):
        #     for point_x in range (house_x, (battery_x + 1)):
        #         self.points_list.append((point_x, point_y))

        # assert len(self.points_list) > 0, f"{house_y}, {battery_y}, {house_x}, {battery_x}"
        
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
        
            

