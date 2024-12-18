# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:25:35 2024

@author: myheartUnderSnow
"""

import pandas as pd 
import math
import matplotlib.pyplot as plt 
import numpy as np


path = r'C:\My Data\VersaStudio\DataDec\12.16.24 -CV-OCP\OCP_650_Ni_FLiNaK_12_16_24.csv'

f = pd.read_csv(path); 

V = f['Potential (V)']
t = f['Elapsed Time (s)']

plt.plot(t,V)
plt.xlabel('ELapsed Time (s)')
plt.ylabel('Potential (V)')
plt.grid() 

plt.title('OCP Taken of 40g FliNaK salt at $500^\circ$C at 1445 on 12/04/24')


