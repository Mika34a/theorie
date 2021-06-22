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
        Returns True if battery still has capacity otherwise False.
        """
        return self.capacity_left

    def start_capacity(self):
        """
        Returns the value of the start_capacity attribute.
        """
        return self.start_capacity

    def reset(self):
        """
        Changes the value of capacity to the start_capacity.
        """
        self.capacity = self.start_capacity

    def output_capacity_refill(self, house):
        """
        Refills a Battery's capacity by adding the house output
        to it's capacity attribute.
        """
        self.capacity = self.capacity + house.output

    def __str__(self) -> str:
        """
        Returns the Battery id in a string.
        """
        return f"Battery: {self.id}"

    def __eq__(self, o: object) -> bool:
        """
        Makes sure that we can compare different batteries by checking
        whether two elements are both Battery, and whether they have the
        same name.
        """
        return self.id == o.id
    
    def __hash__(self) -> int:
        """
        Makes sure we can usee batteries as keys in a dictionary.
        """
        return id(self)
    
    def __ne__(self, o: object) -> bool:
        """
        Make sure we can compare different batterues by checking
        whether two elements are not Battery, and whether they have a
        different name.
        """
        return self.id != o.id


