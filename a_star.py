# a_star.py

import sys
import time

import numpy as np

from matplotlib.patches import Rectangle

import point
import random_map
import math

class AStar:
    def __init__(self, map):
        self.map=map
        self.open_set = []
        self.close_set = []

    def BaseCost(self, p):
        x_dis = p.x
        y_dis = p.y
        # Distance to start point
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def HeuristicCost(self, p):
        x_dis = self.map.size - 1 - p.x
        y_dis = self.map.size - 1 - p.y
        # Distance to end point
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def TotalCost(self, p):
        return self.BaseCost(p) + self.HeuristicCost(p)

    def IsValidPoint(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= self.map.size or y >= self.map.size:
            return False
        return not self.map.IsObstacle(x, y) 
    def IsInPointList(self, p, point_list):
        for point in point_list:
            if point.x == p.x and point.y == p.y:
                return True
        return False

    def IsInOpenList(self, p):
        return self.IsInPointList(p, self.open_set)

    def IsInCloseList(self, p):
        return self.IsInPointList(p, self.close_set)

    def IsStartPoint(self, p):
        return p.x == 0 and p.y ==0

    def IsEndPoint(self, p):
        return p.x == self.map.size-1 and p.y == self.map.size-1


    def ProcessPoint(self, x, y, parent):
        if not self.IsValidPoint(x, y):
            return # Do nothing for invalid point
        p = point.Point(x, y)
        if self.IsInCloseList(p):
            return # Do nothing for visited point
        print('Process Point [', p.x, ',', p.y, ']', ', cost: ', p.cost)
        if not self.IsInOpenList(p):
            p.parent = parent
            p.cost = self.TotalCost(p)
            self.open_set.append(p)

    def SelectPointInOpenList(self):
        index = 0
        selected_index = -1
        min_cost = sys.maxsize
        for p in self.open_set:
            cost = self.TotalCost(p)
            if cost < min_cost:
                min_cost = cost
                selected_index = index
            index += 1
        return selected_index

    def Path(self, p):
        path = []
        while True:
            path.insert(0, p) # Insert first
            

            if self.IsStartPoint(p):
                break
            else:
                p = p.parent
        return path

    def RebuildPath(self,p, plt):
        pointx = []
        pointy = []
        for p in self.Path(p):
            pointx.append(p.x+0.5)
            pointy.append(p.y+0.5)
        i=0
        while True:
            if i< (len(pointx)-1):
                i=i+1
            else:
                break
            a = [pointx[i],pointx[i-1]]
            b = [pointy[i],pointy[i-1]]
            plt.plot(a,b ,color = 'b')
        z= (len(pointx)-1)
        while z > 0 :
            q= 2
            a= [pointx[z],pointx[z-q]]
            #self.checkline(a).append([pointx[z],pointx[z+q]])
            b= [pointy[z],pointy[z-q]]
            #self.checkline(b).append([pointy[z],pointy[z+q]])

            if self.checkline(a,b,plt)== True:
                for k in range(q-1,0,-1):
                    pointx.remove(pointx[z-q+k])
                    pointy.remove(pointy[z-q+k])
                z=z-1
                    
            else:
                z=z-q+1
            

        
    
        j=0
        print(len(pointx),len(pointy))
        while True:
            if j< (len(pointx)-1):
                j=j+1
            else:
                break
            a = [pointx[j],pointx[j-1]]
            b = [pointy[j],pointy[j-1]]
            plt.plot(a,b ,color = 'r')


    def checkline(self,a,b,plt):
        #a=[]
        #b=[]
        c= a[0] - a[1]
        c1 = abs(c)
        d= b[0] - b[1]
        d1 = abs(d)
        for t in range(1,int(c1)+1):
            x = min(a)//1 + t
            y = ((x-a[1])*d/c+b[1])//1
            #plt.plot([x,x+1],[y,y+1] ,color = 'm')
            #plt.plot([x+1,x],[y,y+1] ,color = 'm')
            if self.IsValidPoint(x,y) == False:
                return False
        for t in range(1,int(d1)+1):
            y = min(b)//1 + t
            x = ((y-b[1])*c/d+a[1])//1
            #plt.plot([x,x+1],[y,y+1] ,color = 'm')
            #plt.plot([x+1,x],[y,y+1] ,color = 'm')
            if self.IsValidPoint(x,y) == False:
                return False
        return True




        
            



                
            

    
    def RunAndSaveImage(self, ax, plt):

        start_point = point.Point(0, 0)
        start_point.cost = 0
        self.open_set.append(start_point)

        while True:
            index = self.SelectPointInOpenList()
            if index < 0:
                print('No path found, algorithm failed!!!')
                return
            p = self.open_set[index]
            #rec = Rectangle((p.x, p.y), 1, 1, color='c')
            #ax.add_patch(rec)
            #plt.figure(0.01)
            #plt.clf()
            #plt.pause(0.1)
            #self.SaveImage(plt)

            if self.IsEndPoint(p):
                #return self.BuildPath(p, ax, plt, start_time)
                return self.RebuildPath(p, plt)

            del self.open_set[index]
            self.close_set.append(p)

            # Process all neighbors
            x = p.x
            y = p.y
            #self.ProcessPoint(x-1, y+1, p)
            self.ProcessPoint(x-1, y, p)
            #self.ProcessPoint(x-1, y-1, p)
            self.ProcessPoint(x, y-1, p)
            #self.ProcessPoint(x+1, y-1, p)
            self.ProcessPoint(x+1, y, p)
            #self.ProcessPoint(x+1, y+1, p)
            self.ProcessPoint(x, y+1, p)

