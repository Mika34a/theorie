# Theory - Smartgrid
## Merel Florian, Michael Verdel and Joshua van Zanten
## Programmeangirls

## Purpose
This program includes 4 algorithms to connect houses to batteries in a grid of 51x51.
Included are a random, greedy random, hillclimber and simulated annealing algorithm.
In addition, all algorithms can be run with or without shared connections. All algorithms make sure that the capacity of the batteries is not exceeded and that all houses are connected.

## Getting Started

### Requirements

- Pip and Sass: sudo apt install python3-pip ruby-sass -y 
- Python 3
- Matplotlib: sudo apt-get install python3-matplotlib.
- Numpy: pip install numpy

optional: 
- Check50: see https://theorie.mprog.nl/installatie/start

### Installation guide
1. Copy the link of this repository on GitHub: https://github.com/Mika34a/theorie.git
2. Move to your home directory using cd.
3. Run git clone repository_url https://github.com/Mika34a/theorie.gitin your terminal window.
4. Change your directory into the one that is created. 
5. Open the repository in your code editor. 
    If you use VS Code, run code . to open the repository.  

### Usage      
1. "Usage: python3 main.py [district_number] random/greedy/climber/sim shared:y/n") 
    - example: python3 main.py 1 random shared:y
2. open output/output.json and grid.gridtest.png to see results
3. check results with: check50 -l minprog/theorie-check50/2021/smartgrid 

## The case - Smartgrid
In Smartgrid, the main goal is to connect all 150 houses to 5 batteries without exceeding capacity. The challenge
lies in keeping the price of the connections as low as possible by keeping the connections as short as possible. Every segment costs €9. Batteries also have a price. The total cost of a solution includes the sum of the total cost of the batteries and segments. Connections can either be shared or not shared. When connections are shared, only the first cable on the segment will be counted in the total cost of segments.

## Features
### Random algorithm
This algorithm makes a list of randomly ordered houses and a list of randomly ordered batteries. Subsequently, every house will be connected to the batteries in order of the lists. If the capacity of the first battery in the list is exceeded, the next battery will be chosen. This continues until all houses are connected. The algorithm will repeat until the connections dictionary has the same length as the amount of houses that need to be connected. When repeated, the lists are randomized again in hope of finding a better solution. 

### Random Greedy algorithm
This algorithm makes a list of randomly ordered houses. The greedy behaviour is achieved by making dictionary of batteries for every house ordered by distance. The algorithm will connect each house to the closest battery with enough capacity. This algorithm is repeated until all houses have been connected. With every repetition, the houses list gets a new random order to find a better solution.

### Hill climber
The hillclimber starts with a solution of the random greedy algorithm. After this, the algorithm will remove 5 random connections and will reconnect them randomly until all houses are connected. 
The amount of iterations is by default 10.000 but can be changed in main.py (IT).

### Simulated annealing
Simulated annealing inherits most functions of the Hillclimber. To prevent the hillclimber from getting stuck in a local minimum, we added a descending temperature value that influences the proability of acceptance for every solution. By excepting some bad outcomes in the beginning, the hillclimber gets a chance to escape local minima.
By default, our algorithm has a beginning acceptance chance of 20%. This can be altered by changing the temperature according to the following formula: chance = e^(cost_old - cost_new / temperature). By increasing the starting temperature, or lowering the amount of iterations you can increase the slope of the acceptance chance. Doing the opposite, will decrease the slope.

### Shared function
The shared function enables a user to choose if costs are calculated with or without shared connections.The function calculates the price by putting all segments in a set, which automatically prevents any repetition of segments. the price is then calculated by the amount of segments in the set. 
Filling in "shared:y" results in shared connections. "shared:n" results in costs when connections are not shared.

## Acknowledgements 
We want to thank all teaching assistants from the minor of programming at the UvA that helped us with all our questions. A special thanks to Quinten van der Post and Björn Out for our weekly meetings.

Our simulated annealing and hillclimber algorithm are highly inspired by the live coding lectures from Quinten van der Post and Wouter Vrielink.
