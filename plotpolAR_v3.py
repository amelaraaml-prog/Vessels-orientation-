# -*- coding: utf-8 -*-
"""
Spyder Editor

@rm
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# TO CHANGE
# ===============================================================
pn = "/Users/amelamara/Desktop/Vessel orientation/"
s = [200,250,600] # max values

ts = [50, 100, 50] # each incrémentation
# ===============================================================
# TO CHANGE depending on your file name
fn = 'weights.xlsx'

mydata = pd.read_excel(pn + fn)

ech = [np.linspace(0,250,int(np.floor((s[1]/ts[0])+1))),
       np.linspace(0,250,int(np.floor((s[1]/ts[0])+1))),
       np.linspace(0,250,int(np.floor((s[1]/ts[0])+1))),
       np.linspace(0,250,int(np.floor((s[1]/ts[0])+1))), 
       np.linspace(0,250,int(np.floor((s[1]/ts[0])+1))),
       np.linspace(0,250,int(np.floor((s[1]/ts[0])+1)))]

info_array = mydata.shape

for x in range(info_array[1]):
            
    etiq = mydata.columns[x]
    mydatabar = []
    mydatabar = mydata[etiq]
    color = "gray"

    lowerLimit = 0
    
    plt.figure(figsize=(20,10)) # if you want to improve image quality == 600 
    
    ax = plt.subplot(111, polar=True)
    
    plt.axis('on')
    
    max = ech[x].max()
    slope = (max - lowerLimit) / max
    heights = slope * mydatabar + lowerLimit
    width = np.pi / len(mydatabar.index)
    indexes = list(range(0, len(mydatabar.index)))
    angles = [(element * width) + width/2 for element in indexes]
           
    bars = ax.bar(
        x=angles,
        height=heights, 
        width=width, 
        bottom=lowerLimit,
        linewidth=2, 
        edgecolor="white",
        facecolor=color,
        alpha=1)
    
    ax.set_rmax(max)
    ax.set_rticks(ech[x])
    
    ax.spines['polar'].set_visible(True)   
    plt.title(etiq)
    print('Saving ' + etiq)
    plt.savefig(pn + etiq  + '.svg')
    
print('take your seat and be happy !')