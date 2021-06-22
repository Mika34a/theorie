# house.py
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
        Returns False if house isn't connected yet, otherwise True.
        """
        return self.connected

    def reset(self):
        """
        Changes the connected attribute of a House to False.
        """
        self.connected = False

    def output(self):
        """
        Returns the output as a float of a house.
        """
        return self.output
    
    def __str__(self) -> str:
        """
        Returns the House id in a string.
        """
        return f"House: {self.id}"

