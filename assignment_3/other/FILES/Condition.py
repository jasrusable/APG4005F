import numpy as np
from math import*
from Triangulation import*
from sympy import*
from numpy import*

##j = 0
##for j in range(10):
L = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
for i in range(20):
    file = open('points.txt', 'r')
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
        #print (coord)
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
    lstC = []
    Lmx  = []

    for o in obs1:

        Stat = point[o['station']]
        Targ = point[o['target']]
        X0,Y0 = Stat['Coord'][0],Stat['Coord'][1]
        X1,Y1 = Targ['Coord'][0],Targ['Coord'][1]
        d01 = (X1-X0)**2+(Y1-Y0)**2

        P = (206264.8/3600)*(pi/180)
        a01,b01 = ((X1-X0)/d01)*P ,  ((Y1-Y0)/d01)*P
        angle = arctan2((Y1-Y0),(X1-X0))
        
        if ((angle)<0):
            angle = angle + 2*pi


        else:
            angle=angle

       
        

        observed_angle = float(o['obser'])*(pi/180.0)
        Lmx+=[[observed_angle-angle]]
        rowA = [0.0] * len(unklst)
        #print (angle)
        #rowC = [0.0] * len(unklst)
        if(Stat['Status'] == 0):
            index = unklst.index(Stat['Name']+'_x')
            rowA[index] = b01
            index = unklst.index(Stat['Name']+'_y')
            rowA[index] = -a01
            
            if (Stat['Name'] =='B' and Targ["Name"]== 'Q'):
                rowC = [0.0] * len(unklst)
     
                Cbx = 2*(X0-X1)
                Cby = 2*(Y0-Y1)
                Cqx = -2*(X0-X1)
                Cqy = -2*(Y0-Y1)
                index = unklst.index(Stat['Name']+'_x')
                rowC[index] = Cbx 
                index = unklst.index(Stat['Name']+'_y')
                rowC[index] = Cby
                index = unklst.index(Targ['Name']+'_x')
                rowC[index] = Cqx
                index = unklst.index(Targ['Name']+'_y')
                rowC[index] = Cqy
                w = (X0-X1)**2 + (Y0-Y1)**2 - 54.55**2
  
               # print (rowC)




        if(Targ['Status'] == 0):
            index = unklst.index(Targ['Name']+'_x')
            rowA[index] = -b01
            index = unklst.index(Targ['Name']+'_y')
            rowA[index] = a01


        lstA += [rowA]
       

    


   
    LL = np.matrix(Lmx)
    print (LL)
    C = np.matrix(rowC)

    A = np.matrix(lstA)
    N = A.T*A
    Qkk = -(C*N.I*C.T).I
    E = -N.I*C.T*Qkk
    Qxx = N.I - E*C*N.I
    X = Qxx*A.T*LL-E*w


    xb,yb = X[0,0],X[1,0]
    xc,yc = X[2,0],X[3,0]
    xp,yp = X[4,0],X[5,0]
    xq,yq = X[6,0],X[7,0]



    L[0],L[1],L[2],L[3],L[4],L[5]=[0,0],[xb,yb],[xc,yc],[0,0],[xp,yp],[xq,yq ]






