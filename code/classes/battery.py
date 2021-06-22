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

    # def bat_id(self):
    #     """
    #     Returns the id as int
    #     """
    #     # returns id of the battery
    #     return self.id

    def start_capacity(self):
        """
        Returns the value of the start_capacity attribute
        """
        return self.start_capacity

    def reset(self):
        """
        Changes the value of capacity to the start_capacity
        """
        self.capacity = self.start_capacity

    def output_capacity_refill(self, house):
        """
        Returns True if battery still has capacity otherwise False
        """
        self.capacity = self.capacity + house.output

    def __str__(self) -> str:
        """
        Returns True if battery still has capacity otherwise False
        """
        return f"Battery: {self.id}"

    def __eq__(self, o: object) -> bool:
        """
        Returns True if battery still has capacity otherwise False
        """
        return self.id == o.id
    
    def __hash__(self) -> int:
        """
        Returns True if battery still has capacity otherwise False
        """
        return id(self)
    
    def __ne__(self, o: object) -> bool:
        """
        Returns True if battery still has capacity otherwise False
        """
        return self.id != o.id


