import numpy as np
from math import *
import csv
from a_element_func import *
from b_element_func import *

f = open('POINTS.csv','r')
fixed = {}
free = {}
allpoints={}
l_list = []
for line in f:
    s=line.split(',')

    typestation = float(s[3])
    x,y=float(s[1]),float(s[2])
    name=s[0] #khume did this i don't know how
    allpoints[name]=(x,y)

    if typestation > 0:
        fixed[s[0]] = [float(s[1]),float(s[2])]

    else:
        free[s[0]] =  [float(s[1]),float(s[2])]
    #print (allpoints)

g = open('OBSERVATIONS.csv','r')
directions = []
distances = []
Alist = []
for line2 in g:
    line2=line2.rstrip('\n')

    r=line2.split(',') 
    c_stat = r[0]
    c_targ = r[1]
    observed = r[2]
    

    station_coord,target_coord= allpoints[c_stat],allpoints[c_targ]

    direction = atan((allpoints[c_targ][1]-allpoints[c_stat][1])/(allpoints[c_targ][0]-allpoints[c_stat][0]))
    directions += [direction]
    
    
    distance = sqrt(((allpoints[c_targ][1]-allpoints[c_stat][1])**2)+((allpoints[c_targ][0]-allpoints[c_stat][0])**2))
    distances += [distance]

    #print (a_element(allpoints[c_targ][0],allpoints[c_stat][0],distance), c_stat, c_targ)
    #print (b_element(allpoints[c_targ][1],allpoints[c_stat][1],distance), c_stat, c_targ)

    
##    if c_stat == 'A':
##        #print (c_targ)
##        if c_targ == '
##        dxB = p*(c_stat - dxB)/
##        dyB = 
##        Alist += [[dxB,dyB,dxC,dyC,dxQ,dyQ,dxP,dyP,]]
##
##    elif c_stat == 'B':
##        #print ('B')
##        Alist += [[dxB,dyB,dxC,dyC,dxQ,dyQ,dxP,dyP,]]
##
##    elif c_stat == 'C':
##
##        Alist += [[dxB,dyB,dxC,dyC,dxQ,dyQ,dxP,dyP,]]
##
##    elif c_stat == 'D':
##
##        Alist += [[dxB,dyB,dxC,dyC,dxQ,dyQ,dxP,dyP,]]
##
##    else:
##        continue
##    
##    
    
    mis = (float(observed)*(pi/180))-direction
    x,y = (float(observed)*(pi/180)),direction
    #print (x,y)
    l_list+= [mis]
    l = np.matrix(l_list).T






