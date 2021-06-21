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
    
    def output_capacity_refill(self, house):
        self.capacity = self.capacity + house.output

    def __str__(self) -> str:
        return f"Battery: {self.id}"

    def __eq__(self, o: object) -> bool:
        return self.id == o.id
    
    def __ne__(self, o: object) -> bool:
        return self.id != o.id
