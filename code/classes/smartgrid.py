# smartgrid.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements Connection class.

class Smartgrid():

    # functions
    # - connect batteries with houses 
    # - return total costs of connections and batteries 
    # - return houses if not connected
    # - return batteries with capacity left

    def __init__(self):
        """
        Initializes the Smartgrid class.
        """
        pass

    def connect(self, battery, house):
        connection = Connection(house, battery)
        return connection

    def costs(self, connection):
        """
        Returns the total costs of the combined cables.
        """
        # laying a cable costs 9 per grid
        # costs for each battery is 5000, with each district having 5 batteries
        cost_grid = 9
        cost_battery = 5000
        cost_cable = length * cost_grid

    def disc_houses(self):
        """
        Returns the houses that have not been connected.
        """
        pass

    def batteries_left(self):
        """
        Returns the batteries that still have leftover capacity.
        """
        pass


