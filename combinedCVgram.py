# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:58:26 2024

@author: myheartUnderSnow
"""

import pandas as pd 
import math
import matplotlib.pyplot as plt 
import numpy as np


path1 = r'C:\My Data\VersaStudio\DataDec\12.11.24 -CV-OCP\CV_650_Ni_FLiNaK_12_11_24_50mV_0Vto-1to1to-0.9.csv'
path2 = r'C:\My Data\VersaStudio\DataDec\12.11.24 -CV-OCP\CV_650_Ni_FLiNaK_12_11_24_100mV_0Vto-1to1to-0.9.csv'
path3 = r'C:\My Data\VersaStudio\DataDec\12.11.24 -CV-OCP\CV_650_Ni_FLiNaK_12_11_24_200mV_0Vto-1to1to-0.9.csv'

f1 = pd.read_csv(path1); 
f2 = pd.read_csv(path2);
f3 = pd.read_csv(path3);

V1 = f1['Potential (V)']
a1 = f1['Current (A)']

V2 = f2['Potential (V)']
a2 = f2['Current (A)']

V3 = f3['Potential (V)']
a3 = f3['Current (A)']

plt.plot(V1,a1, label='50mV/s')
plt.plot(V2,a2, label='100mV/s')
plt.plot(V3,a3, label='200mV/s')
plt.ylabel('Current (Amps)')
plt.xlabel('Potential (V)')
plt.grid() 
plt.legend(loc='upper left')
plt.title('12-11 0V->-1V->1V->-0.9V CV sweeps taken with 40g FLiNaK at $650^\circ$C')
