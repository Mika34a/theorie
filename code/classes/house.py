# House.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements House class.

class House:
    def __init__(self, x_coordinate, y_coordinate, output, connected):
        """
        Initializes House class.
        """
        # attributes 
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.output = output
        self.connected = False
     