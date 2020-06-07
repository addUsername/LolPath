# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:56:49 2020

@author: SERGI
"""

import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import math
import json
import os
import numpy as np
from matplotlib._png import read_png


class Plotting:

    def __init__(self, title, champions):

        self.title = title
        self.champions = champions
        self.champions_dict = {}
        self.readJson()

    def writeJson(self):
        #ojo con esto que sobrescribe
        with open(os.getcwd()[:len(os.getcwd())-13]+"visualization\\outputs\\"+self.title+".json","w") as file: 
            json.dump(self.champions_dict, file)
            
    def readJson(self):
        #Asi nos saltamos tener q analizar el video, lo pillamos de aqui e ya.
        print(os.getcwd()[:len(os.getcwd())-13]+"visualization\\outputs\\"+self.title+".json")
        with open(os.getcwd()[:len(os.getcwd())-13]+"visualization\\outputs\\"+self.title+".json","r") as file:
            self.champions_dict = json.load(file)
            print(len(self.champions_dict))
    
    def dist(a,b):
        return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
            
    def generatePlot(self, dist, num_points):
        #..\\resources\\inicial.png
        #path=(Path("visualization/resources/") / "inicial.png" )
        imageFile = cbook.get_sample_data(os.getcwd()[:len(os.getcwd())-13]+"visualization\\resources\\inicial.png")
        image = plt.imread(imageFile)
        plt.imshow(image)
        plt.suptitle(self.title, fontsize=14, fontweight='bold')
    
        print (self.champions_dict[self.champions[0]][5])
        x=[]
        y=[]
        #pos_pre=self.champions_dict[self.champions[0]][0]   
        for i in range(1,len(self.champions_dict[self.champions[0]])-1):
            if (self.champions_dict[self.champions[0]][i]!= None):
                x.append(self.champions_dict[self.champions[0]][i][0])
                y.append(self.champions_dict[self.champions[0]][i][1])
            else:
                plt.plot(x,y,'b-')
                x=[]
                y=[]                
        plt.plot(x,y,'b-',label=self.champions[0])
    
        x=[]
        y=[]
        #pos_pre=self.champions_dict[self.champions[0]][0]   
        for i in range(1,len(self.champions_dict[self.champions[1]])-1):
            if (self.champions_dict[self.champions[1]][i]!= None):
                x.append(self.champions_dict[self.champions[1]][i][0])
                y.append(self.champions_dict[self.champions[1]][i][1])
            else:
                plt.plot(x,y,'r-')
                x=[]
                y=[]                
        plt.plot(x,y,'r-',label=self.champions[1])     
        
        x=[]
        y=[]
        for i in range(1,len(self.champions_dict[self.champions[2]])-1):
            if (self.champions_dict[self.champions[2]][i]!= None):
                x.append(self.champions_dict[self.champions[2]][i][0])
                y.append(self.champions_dict[self.champions[2]][i][1])
            else:
                plt.plot(x,y,'g-')
                x=[]
                y=[]                
        plt.plot(x,y,"g-", label=self.champions[2])
        
        x=[]
        y=[]
        for i in range(1,len(self.champions_dict[self.champions[3]])-1):
            if (self.champions_dict[self.champions[3]][i]!= None):
                x.append(self.champions_dict[self.champions[3]][i][0])
                y.append(self.champions_dict[self.champions[3]][i][1])
            else:
                plt.plot(x,y,'y-')
                x=[]
                y=[]
                
        plt.plot(x,y,'y-',label=self.champions[3])
        
        for i in range(1,len(self.champions_dict[self.champions[4]])-1):
            if (self.champions_dict[self.champions[4]][i]!= None):
                x.append(self.champions_dict[self.champions[4]][i][0])
                y.append(self.champions_dict[self.champions[4]][i][1])
            else:
                plt.plot(x,y,'k-')
                x=[]
                y=[]
                
        plt.plot(x,y,'k-',label=self.champions[4])
        
        
        
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.savefig(os.getcwd()[:len(os.getcwd())-13]+"visualization\\outputs\\"+self.title+".png")
        plt.savefig(os.getcwd()[:len(os.getcwd())-13]+"visualization\\outputs\\"+self.title+".pdf")
        plt.show()
        
    def generate3Dplot(self,champs,colors):
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        
        '''
        para poner la imagen de fondo.. consume muchos recursos..xd
        fn = cbook.get_sample_data(os.getcwd()[:len(os.getcwd())-13]+"visualization\\resources\\inicial.png", asfileobj=False)
        img = read_png(fn)
        x, y = np.ogrid[0:img.shape[0], 0:img.shape[1]]
        
        ax.plot_surface(x, y, np.zeros((len(x),len(y))) , rstride=1, cstride=1, facecolors=img)
        '''
        #pos_pre=self.champions_dict[self.champions[0]][0]
        for idx, champion_name in enumerate(champs):
            x=[]
            y=[]
            z=[]
            time=0
            print(len(self.champions_dict[champion_name]))
            for i in range(1,len(self.champions_dict[champion_name])-1):
                
                if (self.champions_dict[champion_name][i]!= None):
                    x.append(self.champions_dict[champion_name][i][0])
                    y.append(self.champions_dict[champion_name][i][1])
                    z.append(time)
                
                time+=1
            ax.plot3D(x, y, z, color=colors[idx])
            ax.scatter3D(x, y, z, c=z, cmap='hsv');
            
            #axix xy path
            ax.plot3D(x, y, np.zeros(len(z)), color=colors[idx])
            print("3Dplot: "+champion_name)
            
        plt.show()
    
    def generate3DSurface(self,champs,colors,num):
        
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        #ax = Axes3D(fig)
        
        for idx, champion_name in enumerate(champs):
            
            '''
            x =  np.arange(start=0, stop=250, step=2*num)
            y = np.arange(start=0, stop=250, step=2*num)
            '''
            x = np.arange(int(math.sqrt(num)))
            y = np.arange(int(math.sqrt(num)))
            z=np.zeros((len(x),len(y)))
            for i in range(1,len(self.champions_dict[champion_name])-1):
                
                if (self.champions_dict[champion_name][i]!= None):                   
                    col , row = self.makeCount(self.champions_dict[champion_name][i],num)
                    z[row-1][col-1] += 1
                    
            #bottom = np.zeros_like(z)
            #z_array=np.asarray(z) 
            
            #ax.bar3d(x, y, bottom, num, num, z, shade=True)
            xx, yy = np.meshgrid(x, y)
            ax.plot_surface(xx, yy, z, cmap=plt.cm.viridis, cstride=1, rstride=1)
            
            print("3Dsurface: "+champion_name)
        plt.show()
        
    def makeCount(self,pos,num):
        
        
        a=int(pos[0]/(2*num))
        b=int(pos[1]/(2*num))
        return [a,b]
        
