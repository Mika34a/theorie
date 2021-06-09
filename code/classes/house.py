# House.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements House class.

class House:
    def __init__(self, x_coordinate, y_coordinate, output, connected, id):
        """
        Initializes House class.
        """
        # attributes 
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.id = id
        self.output = output
        self.connected = False
    
def check_connection(self):
    """
    Returns False if house isn't connected yet, otherwise True
    """
    return self.connected
    
def house_id(self):
    """
    Returns the house id as int
    """
    return self.id

def output(self):
    return self.output