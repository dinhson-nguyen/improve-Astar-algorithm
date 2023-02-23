# random_map.py

import numpy as np

import point

class RandomMap:
    def __init__(self, size=50):
        self.size = size
        #self.obstacle = size//8
        self.obstacle = 15
        self.GenerateObstacle()

    def GenerateObstacle(self):
        self.obstacle_point = []
        z = np.random.randint(4, 9)
        for t in range (0, z+1):
            for g in range(0,z+1):
                self.obstacle_point.append(point.Point(self.size//2+t, self.size//2+g))

        for i in range(self.obstacle-1):
            x = np.random.randint(0, self.size -9)
            y = np.random.randint(0, self.size-9)
            self.obstacle_point.append(point.Point(x, y))

            #if (np.random.rand() > 0.5): # Random boolean
            if True: # Random boolean
                z = np.random.randint(3, 9)
                for t in range (0, z+1):
                    for g in range(0,z+1):
                        self.obstacle_point.append(point.Point(x+g, y+t))
        
    def nearobstacle(self,i,j):
        self.near = []
        for t in range(self.size):
            for h in range (self.size):
                if self.IsObstacle(t,h) == True:
                    if self.IsObstacle(t+1,h+1)== True:
                        self.near.append(point.Point(t+1,h))
                    if self.IsObstacle(t+1,h-1)== True:
                        self.near.append(point.Point(t+1,h))
        for p in self.near:
            if i == p.x and j == p.y:
                return True
        return False
        
    def IsObstacle(self, i ,j):
        for p in self.obstacle_point:
            if i==p.x and j==p.y:
                return True
        return False