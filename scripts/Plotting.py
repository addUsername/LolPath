# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:56:49 2020

@author: SERGI
"""

import matplotlib.pyplot as plt
from matplotlib import cbook
import math
import json

class Plotting:
        
    
    def __init__(self,title,champions):
        
        self.title = title
        self.champions = champions
        self.champions_dict={}
        
        
    def writeJSON(self):
        
        with open(os.getcwd()[:len(os.getcwd())-13]+"visualization\\outputs\\"+self.title+".json","w") as file: 
            json.dump(self.champions_dict, file)
            
    def readJson(self):
        #Asi nos saltamos tener q analizar el video, lo pillamos de aqui e ya.
        with open(os.getcwd()[:len(os.getcwd())-13]+"visualization\\outputs\\"+self.title+".json","r") as file:
            self.champions_dict = json.load(file)
            #print(self.champions_dict)
    
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
    
