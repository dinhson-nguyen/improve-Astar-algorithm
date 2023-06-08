# random_map.py

import numpy as np

import point

class RandomMap:
    def __init__(self, size=50):
        self.size = size
        #self.obstacle = size//8
        self.obstacle = 15
        self.GenerateObstacle()
        self.risk()

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
        
    def risk(self):
        self.risk_inside = []
        self.risk_outside = []
        for t in range(self.size):
            for h in range (self.size):
                if self.IsObstacle(t,h) == True:
                    for m in range(-1,2,1):
                        for n in range(-1,2,1):
                            if self.IsObstacle(t+m,h+n)== False:
                                self.risk_inside.append(point.Point(t+m,h+n))
        
        for t in range(self.size):
            for h in range (self.size):
                if self.Is_risk_inside(t,h):
                    
                    for m in range(-1,2,1):
                         for n in range(-1,2,1):
                             if self.Is_risk_inside(t+m,h+n) ==False:
                                if self.IsObstacle(t+m,h+n)== False:
                                    self.risk_outside.append(point.Point(t+m,h+n))
        
    def Is_risk_inside(self,i,j):
        for p in self.risk_inside:
            if i == p.x and j == p.y:
                return True
        return False

    def Is_risk_outside(self,i,j):
        for p in self.risk_outside:
            if i == p.x and j == p.y:
                return True
        return False
    def IsObstacle(self, i ,j):
        for p in self.obstacle_point:
            if i==p.x and j==p.y:
                return True
        return False