# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:58:26 2024

@author: myheartUnderSnow
"""

import pandas as pd 
import math
import matplotlib.pyplot as plt 
import numpy as np


path = r'C:\My Data\VersaStudio\DataDec\12.16.24 -CV-OCP\CV_650_Ni_FLiNaK_12_16_24_0to-1to1to-0.9_50mV.csv'

f = pd.read_csv(path); 

V = f['Potential (V)']
a = f['Current (A)']

plt.plot(V,a, color='green')
plt.ylabel('Current (Amps)')
plt.xlabel('Potential (V)')
plt.grid() 
plt.title('0V->-2V 50mV/s CV sweep taken with 40g FLiNaK at $500^\circ$C')
