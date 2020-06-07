# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:57:43 2020

@author: SERGI
"""

from scripts.Analytics import Analytics as ana
from scripts.Plotting import Plotting as plo
from scripts.Neural import Neural as neu
import os
import pandas as pd
def main():

    champions = ["AmumuO","CaitlynO","FizzO","DariusO","MorganaO"]
    
    #(self, threshold, second_inicial, frame_step, frame_stop)
    # backslash
    #video = ana(os.getcwd()[:len(os.getcwd())-13]+"visualization/resources/videoHD.mp4" , champions)
    #video.readVideo(0.33,1000,1,3000)
    #video.writeVideo("threshold0.33_noCNN34")
    
    
    #plot = plo("threshold0.33_noCNN34",champions)
    abdist=50 #distancia maxima entre dos puntos
    abnum=8  #max not registred num
    #plot.generatePlot(abdist,abnum)
    colors=["red","blue","green","yellow","orange"]
    champs=set(("AmumuO","CaitlynO","FizzO","DariusO","MorganaO"))
    #plot.generate3Dplot(champs,colors)
    
    #plot.generate3DSurface(["MorganaO"],["red"],25) #Mejorar esto.. pero vamos q ahi estan los datos, YEAH cool
    neural = neu(os.getcwd()[:len(os.getcwd())-13]+"visualization/dataaa/data.json")
    df = neural.readJSON()
    print(str(len(df["featuresRed"][0])) + "x" + str(len(df["featuresRed"][0][0])))
    
    

if __name__== "__main__":
   main()