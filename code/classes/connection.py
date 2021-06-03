# connection.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements Connection class.

class Connection:
    def __init__(self, house, battery, distance):
        """
        Initializes Connection class.
        """
        # attributes 
        self.house = house
        self.battery = battery 
        self.distance = distance
        self.points = []
