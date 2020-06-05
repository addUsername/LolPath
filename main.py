# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:57:43 2020

@author: SERGI
"""

from scripts.Analytics import Analytics as ana
from scripts.Plotting import Plotting as hola
import os

def main():

    champions = ["AmumuO","CaitlynO","FizzO","DariusO","MorganaO"]
    
    #(self, threshold, second_inicial, frame_step, frame_stop)
    video = ana(os.getcwd()[:len(os.getcwd())-13]+"visualization\\resources\\videoHD.mp4" , champions)
    video.readVideo(0.33,500,2,3000)
    video.writeVideo("threshold0.33_noCNN34")
    
    '''
    plot = Plotting(video.title,champions)
    abdist=50 #distancia maxima entre dos puntos
    abnum=8  #max not registred num
    plot.generatePlot(abdist,abnum)
    '''
    
    
    

if __name__== "__main__":
   main()