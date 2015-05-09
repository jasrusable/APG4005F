import numpy as np
from math import*

def genMatrices(point, obs, unklst):
    lstA = []
    Lmx=[]

    for o in obs:
        Stat = point[o['station']]
        Targ = point[o['target']]
        
        X0, Y0 = Stat['Coord'][0], Stat['Coord'][1]
        X1, Y1 = Targ['Coord'][0], Targ['Coord'][1]
        
        d01 = (X1-X0)**2+(Y1-Y0)**2
        
        P = (206264.8/3600.0)*(pi/180.0)
        
        a01, b01 = P*((X1-X0)/d01),  P *((Y1-Y0)/d01)

        angle = np.arctan2((Y1 - Y0),(X1 - X0))       
        if (angle < 0):
            angle = angle + 2*pi
            
        observed_angle = float(o['obser'])*(pi/180.0)

        Lmx += [[observed_angle - angle]]

        rowA = [0.0] * len(unklst)

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

        if(Targ['Status'] == 0):
            index = unklst.index(Targ['Name']+'_x')
            rowA[index] = -b01
            index = unklst.index(Targ['Name']+'_y')
            rowA[index] = a01

        lstA += [rowA]


    vl = np.matrix(Lmx) 
    mA = np.matrix(lstA)
    mC = np.matrix(rowC)


    return vl, mA, mC, w


# Free network

def Freenetwork(point, obs, unklst):
    lstA = []
    Lmx=[]

    for o in obs:
        Stat = point[o['station']]
        Targ = point[o['target']]
        
        X0, Y0 = Stat['Coord'][0], Stat['Coord'][1]
        X1, Y1 = Targ['Coord'][0], Targ['Coord'][1]
        
        d01 = (X1-X0)**2+(Y1-Y0)**2
        
        P = (206264.8/3600.0)*(pi/180.0)
        
        a01, b01 = P*((X1-X0)/d01),  P *((Y1-Y0)/d01)

        angle = np.arctan2((Y1 - Y0),(X1 - X0))       
        if (angle < 0):
            angle = angle + 2*pi
            
        observed_angle = float(o['obser'])*(pi/180.0)

        Lmx += [[observed_angle - angle]]

        rowA = [0.0] * len(unklst)

        if(Stat['Status'] == 0 or Stat['Status'] == 1 ):
            index = unklst.index(Stat['Name']+'_x')
            rowA[index] = b01
            index = unklst.index(Stat['Name']+'_y')
            rowA[index] = -a01

        if(Targ['Status'] == 0 or Targ['Status'] == 1):
            index = unklst.index(Targ['Name']+'_x')
            rowA[index] = -b01
            index = unklst.index(Targ['Name']+'_y')
            rowA[index] = a01

        lstA += [rowA]


    freel = np.matrix(Lmx) 
    freeA = np.matrix(lstA)



    return freel, freeA



# update the adjustment solution
def updateSolution(point, unklst, X):
    for u, corr in zip(unklst, X):
        name = u[:-2]
        suffix = u[-1:]

        if(suffix == 'x'):
            point[name]['Coord'][0] += float(corr)
        else:
            point[name]['Coord'][1] += float(corr)




# check if solution has converged
def hasConverged(x, tolerance):
    convergence = True

    for corr in x:
        if(abs(corr) > tolerance):
            convergence = False
            break

    return convergence
