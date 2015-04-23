import numpy as np
from math import*
from Triangulation import*
from sympy import*
from numpy import*


L = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
for i in range(3):
    file = open('POINTS.csv', 'r')
    f=open('OBSERVATIONS.csv','r')
    point = {}
    INDEX=0
    
    for line in file:
        sp = line.split(',')
        Xcor,Ycor = L[INDEX][0],L[INDEX][1]

        name = sp[0].strip()
        x = float(sp[1])
        y = float(sp[2])
        status = int(sp[3])

        coord = [x+Xcor  , y +Ycor]
        info = {}
        info['Name'] = name
        info['Coord'] = coord

        
        info['Status'] = status
        
        point[name] = info
        INDEX+=1

    unkset = set()
    for name, p in point.items():
        if p['Status'] == 0:
            unkset.add(name + "_x")
            unkset.add(name + "_y")


    unklst = list(unkset)
    unklst.sort()

    obs1=[]
    for observ in f:
        observ=observ.rstrip('\n')
        sp=observ.split(',')
        sta=sp[0]
        targ=sp[1]
        obs1+=[{'station':sta,'target':targ,'obser':sp[2]}]

    lstA = []
    Lmx=[]
    for o in obs1:
        Stat = point[o['station']]
        Targ = point[o['target']]
        X0,Y0 = Stat['Coord'][0],Stat['Coord'][1]
        X1,Y1 = Targ['Coord'][0],Targ['Coord'][1]
        d01 = (X1-X0)**2+(Y1-Y0)**2
        P = (206264.8/3600.0)*(pi/180.0)
        a01,b01 = P*((X1-X0)/d01) ,  P*((Y1-Y0)/d01)
        angle = arctan2((Y1-Y0),(X1-X0))

        
        if (angle<0):
            angle = angle + 2*pi

        else:
            angle=angle
            
        observed_angle = float(o['obser'])*(pi/180.0)

        Lmx+=[[observed_angle-angle]]

        rowA = [0.0] * len(unklst)

        if(Stat['Status'] == 0):
            index = unklst.index(Stat['Name']+'_x')
            rowA[index] = b01
            index = unklst.index(Stat['Name']+'_y')
            rowA[index] = -a01

        if(Targ['Status'] == 0):
            index = unklst.index(Targ['Name']+'_x')
            rowA[index] = -b01
            index = unklst.index(Targ['Name']+'_y')
            rowA[index] = a01

        lstA += [rowA]
    ll = np.matrix(Lmx)

    
    A = np.matrix(lstA)

    
    X = (A.T*A).I*(A.T*ll)


    xb,yb = X[0,0],X[1,0]
    xc,yc = X[2,0],X[3,0]
    xp,yp = X[4,0],X[5,0]
    xq,yq = X[6,0],X[7,0]
    L[0],L[1],L[2],L[3],L[4],L[5]=[0,0],[xb,yb],[xc,yc],[0,0],[xp,yp],[xq,yq ]



V = A*X - l
Sigma = float(V.T*V)
CovX = Sigma*(A.T*A).I







