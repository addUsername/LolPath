# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:56:49 2020

@author: SERGI
"""

import matplotlib.pyplot as plt
from matplotlib import cbook
import math
import json

def __init__(self,title,champions):
    
    self.title = title
    self.champions = champions
    self.data={}
    
    
def readJson(self):

    with open(self.title+".json") as json_file:
        self.data = json.load(json_file)
        
def dist(a,b):
    return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
        
def generatePlot(self, dist, num_points):
    
    imageFile = cbook.get_sample_data("..\\resources\\inicial.png")
    image = plt.imread(imageFile)
    plt.imshow(image)
    plt.suptitle(self.title, fontsize=14, fontweight='bold')

    
    x=[]
    y=[]
    num=0
    pos_pre=self.paths[self.champions[0]][0]    
    for i in range(1,len(self.paths[self.champions[0]])-1):
        if((dist(pos_pre, self.paths[self.champions[0][i]])) < dist):
            pos_pre=self.paths[self.champions[0][i]]
                               
            x.append(pos_pre[0])
            y.append(pos_pre[1])
        elif (num==num_points):
            pos_pre=self.paths[self.champions[0][i]]
            num=0 #???
        num+=1
    plt.plot(x,y,'b-',label="amumu")

