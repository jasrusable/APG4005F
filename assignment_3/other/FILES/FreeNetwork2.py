import numpy as np
from scipy import linalg as LA
from math import*
#from Triangulation import*
from sympy import*
from numpy import*
from adjio import readInfo
from adjmatrices import genMatrices, updateSolution, hasConverged, Freenetwork

class FreenetworkSolution(object):
    def __init__(self, A, P, G, C, I, x, v, l, w):
        self.A = A
        self.P = P
        self.G = G
        self.C = C
        self.I = I
        self.x = x
        self.v = v
        self.l = l
        self.w = w

    @property
    def Qkk(self):
        return -(self.C * self.N.I * self.C.T).I

    @property
    def Qxx(self):
        return self.I * self.C.T * self.Qkk
    

def solve_free(readInfo_epoch_0):
    point = readInfo_epoch_0[0]
    unks = readInfo_epoch_0[1]
    obs = readInfo_epoch_0[2]
    FreeUnknws = readInfo_epoch_0[3]
    maxIterations = 5
    iteration = 0
    converged = False
    while((not converged) or (iteration < maxIterations)):
       # print('Iteration: ', iteration)
        # generate A, and L matrices
        l, A, C, w = genMatrices(point, obs, unks)
        
        # get the solution (Parametric)
        x = (A.T * A).I * (A.T * l)
        converged = hasConverged(x, 0.0001)
        #print ("X matrix: Parametric")

        # get the solution (Condition)
        N   = A.T*A
        Qkk = -(C*N.I*C.T).I
        E   = -N.I*C.T*Qkk
        Qxx = N.I - E*C*N.I
        cX  = Qxx*A.T*l-E*w

        #print ("X matrix: Condition")
        #print (cX)

        # Free network
        fl ,fA  = Freenetwork(point, obs, FreeUnknws)

        ATA = fA.T*fA
        e_vals, e_vecs = LA.eig(ATA)

        E_vector = e_vecs[8],e_vecs[9],e_vecs[10],e_vecs[11]
        G_matrix = np.matrix(E_vector)
        G = G_matrix.T

        N_free   = ATA + G*G.T
        Q_free   = N_free.I

        X_free   = Q_free*fA.T*fl
        #print (X_free)

        # S Transformation

        Id =   [[1,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,1]]
        
        I = np.matrix(Id)

        t1      = -(G.T*I*G).I*G.T*I*X_free
        X_trans = X_free - G*(G.T*I*G).I*(G.T*I)*X_free
                      
        # update unknowns
        updateSolution(point, unks, x)

        # get residuals Parametric
        v = A * x - l

        # least squares criterion Parametric
        vTv = v.T * v

        # increment iteration counter
        iteration += 1

        # sigma 0
        sigma0 = float(vTv)/(12.0) 
     
        # covX Parametric
        covX = sigma0 * (A.T * A).I
    return FreenetworkSolution(A=A, P=None, G=G, C=C, I=I, x=x, v=v, l=l, w=w)


readInfo_epoch_0 = readInfo('data/POINTS.csv', 'data/OBSERVATIONS.csv', 'data/FreeNetwork.csv' )

epoch_0 = solve_free(readInfo_epoch_0)

print(epoch_0.Qxx)
