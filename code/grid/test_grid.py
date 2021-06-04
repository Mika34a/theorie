import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.pyplot import figure

plt.style.use('classic')

figure(figsize=(8, 8), dpi=150)


x = [0,10,20,30,40,50]
y = [0,10,20,30,40,50]

tick_spacing = 1

fig, ax = plt.subplots(1,1)

# Major ticks every 20, minor ticks every 5
major_ticks = np.arange(0, 51, 10)
minor_ticks = np.arange(0, 51, 1)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

# And a corresponding grid
ax.set_facecolor('xkcd:charcoal')
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

#add margins

# points set to always show full graph
plt.plot(0, 0)
plt.plot(50, 50)

# set specific point
plt.plot(34,47, 'bo')



plt.savefig("test")