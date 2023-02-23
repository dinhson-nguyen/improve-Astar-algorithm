# main.py

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

import random_map
import a_star
import math

plt.figure(figsize=(5, 5))

map = random_map.RandomMap()

ax = plt.gca()
ax.set_xlim([0, map.size])
ax.set_ylim([0, map.size])


for i in range(map.size):
    for j in range(map.size):
        if map.IsObstacle(i,j) == False:
            rec = Rectangle((i, j), width=1, height=1, edgecolor='white', facecolor='w')
            ax.add_patch(rec)
        
for i in range(map.size):
    for j in range(map.size):
        if map.IsObstacle(i,j):
            for t in range(-1,2,1):
                for z in range(-1,2,1):
                    if map.IsObstacle(i+z,j+t):
                        pass
                    #else:
                        #rec = Rectangle((i+z, j+t), width=1, height=1, color='gray')
                        #ax.add_patch(rec)
            rec = Rectangle((i, j), width=1, height=1, color='gray')
            ax.add_patch(rec)

               
rec = Rectangle((0, 0), width = 1, height = 1, facecolor='b')
ax.add_patch(rec)

rec = Rectangle((map.size-1, map.size-1), width = 1, height = 1, facecolor='r')
ax.add_patch(rec)

plt.axis('equal')
plt.axis('on')
plt.tight_layout()
#x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19])
#y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19])
#plt.plot(x, y)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)



a_star = a_star.AStar(map)

a_star.RunAndSaveImage(ax, plt)
#x1 = [46, 41]
#y1 =  [20, 30]
#x2, y2 = [1, 10], [3, 2]
#plt.plot( x1, y1, color = 'r')

plt.show()
