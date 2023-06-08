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
            rec = Rectangle((i, j), width=1, height=1, color='black')
            ax.add_patch(rec)

        if map.Is_risk_inside(i,j):
            rec = Rectangle((i, j), width=1, height=1, color='gray')
            ax.add_patch(rec)

        if map.Is_risk_outside(i,j):
            rec = Rectangle((i, j), width=1, height=1, color='lightgray')
            ax.add_patch(rec)
        
        

               
rec = Rectangle((0, 0), width = 1, height = 1, facecolor='b')
ax.add_patch(rec)

rec = Rectangle((map.size-1, map.size-1), width = 1, height = 1, facecolor='r')
ax.add_patch(rec)

plt.axis('equal')
plt.axis('on')
plt.tight_layout()

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)



a_star = a_star.AStar(map)

a_star.RunAndSaveImage(ax, plt)


plt.show()
