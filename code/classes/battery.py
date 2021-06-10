# battery.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements Battery class.

class Battery:
    def __init__(self, x_coordinate, y_coordinate, capacity, id):
        """
        Initializes Battery class.
        """
        # attributes 
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.capacity = capacity
        self.start_capacity = capacity
        self.id = id
        self.capacity_left = True


    def check_capacity(self):
        """
        Returns True if battery still has capacity otherwise False
        """
        return self.capacity_left

    def bat_id(self):
        """
        Returns the id as int
        """
        # returns id of the battery
        return self.id

    def start_capacity(self):
        return self.start_capacity

    def reset(self):
        self.capacity = self.start_capacity
        return
