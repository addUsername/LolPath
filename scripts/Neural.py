# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:21:19 2020

@author: SERGI
"""
import numpy as np
import pandas as pd
import json


class Neural:
    
    def __init__(self, json_path):
        self.json_path = json_path
        
    def readJSON(self, parse = ""):
         with open(self.json_path,"r") as file:
            champions_dict = json.load(file)
            if (parse == "df"):
                return pd.DataFrame(champions_dict)
            return champions_dict