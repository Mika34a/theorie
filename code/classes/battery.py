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
        self.id = id