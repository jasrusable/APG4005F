##PHILLY PILANE
##SPHERE FITTING
##APG4005F
##

import numpy as np
from math import *
import csv
from scipy.stats import chi2

from matplotlib import pyplot
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D


##provisionals
f = open('data_assignment1.csv','r')
xpoints = []
ypoints = []
zpoints = []
####j = 0
for line in f:
    s=line.split(",")
    x = float(s[0])
    y = float(s[1])
    z = float(s[2])
    xpoints.append(x)
    ypoints.append(y)
    zpoints.append(z)

x0=((float(max(xpoints))-float(min(xpoints)))/2.0)+(min(xpoints))
y0=(float(max(ypoints))-float(min(ypoints)))/2.0+(min(ypoints))
z0=min(zpoints)
r0=abs((float(max(zpoints))-float(min(zpoints))))

##j = 0
for i in range(10): ##for iterations
    
    Alist = [] #creating empty lists because zero matrices
    Llist = [] #are harder to work with
    Blist = []
    wlist = [] #creating an empty list for the w matrice
    
##    def read(filename):
    f = open('data_assignment1.csv','r')
    points = []
    j = 0
    for line in f:
        s=line.split(",")
        x = float(s[0])
        y = float(s[1])
        z = float(s[2])
        points+=[x,y,z]

        #if (r0**2)-(x-x0)**2 >= 0: #acounting for the negative difference under square root
       

        dx0= (-2.0)*(x-x0)  ##partials of the observation equation
        dy0= (-2.0)*(y-y0)
        dz0= (-2.0)*(z-z0)
        dr0= (-2.0)*(r0)
        dx = (2.0)*(x-x0)
        dy = (2.0)*(y-y0)
        dz = (2.0)*(z-z0)
        f0 = (x-x0)**2 + (y-y0)**2 + (z-z0)**2 - r0**2
        
        ##Making the A matrix element list
        Alist += [[dx0,dy0,dz0,dr0]]
        
        #######################################################
        ##Making the B matrix element list (Help from Chad Lamb - MSc Student, Tutor)

        b_element = [0]*(len(xpoints)*3)
        b_element[j*3] = dx
        b_element[j*3+1] = dy
        b_element[j*3+2] = dz
        Blist += [b_element]
        j+=1



        wlist += [f0] ##misclosure vector

    A = np.matrix(Alist)

    B = np.matrix(Blist)
    Wt = np.matrix(wlist)
    w = Wt.T
    M = (B*B.T)
    points_adj = np.matrix(points)

    X=-((A.T*(B*B.T).I*A)).I*A.T*((B*B.T).I)*w
    x0 += float(X[0]) 
    y0 += float(X[1])
    z0 += float(X[2])
    r0 += float(X[3])

    k=(-(M.I))*((A*X)+w)
    v=B.T*k
    aposti=((v.T)*v)/((len(A)*3)-len(X)) #a posterioiri variance
    Qxx=(A.T*M.I*A).I #var-cov of unknowns
    
    sigmaxx=float(aposti[0])*Qxx #var-cov of unknowns
    sigmaww=float(aposti[0])*M
    sigmavv=float(aposti[0])*(B.T)*(M.I)*(-A*(A.T*M.I*A).I*A.T+M)*M.I*B
    
    adj =  points_adj.T+v
    pos = 0

    x_plot = []
    y_plot = []
    z_plot = []

##  COMPUTING RADII TO EVERY POINT
    radii=[]
    for n in range(len(A)):
        radii += [(float(adj[pos])-x0)**2+(float(adj[pos+1])-y0)**2+(float(adj[pos+2])-z0)**2 - r0**2]
        
        test = (np.matrix(radii)).I
        x_plot.append(float(adj[pos]))
        y_plot.append(float(adj[pos+1]))
        z_plot.append(float(adj[pos+2]))
        pos+=3

## Print OUTS:
##print ("Best :")
##print ("                  Centre: ","(",round(x0,2),",",round(y0,2),",",round(z0,2),")")
##print ("                  Radiaus: ",round(r0,2),"units")
print ("--------------------------------------------------------")
print ("A-Matrix:", A.shape)
print (A)
print ("--------------------------------------------------------")
print ("B-Matrix:",B.shape)
print (B)
print ("--------------------------------------------------------")
print ("Vector of Unknowns (X):", X.shape)
print (X)
print ("--------------------------------------------------------")
print ("Vector of Residuals (v):", v.shape)
print (v)
print ("--------------------------------------------------------")
print ("σ^2_0 'a posteriori variance':")
print (aposti)
print ("--------------------------------------------------------")
print ("∑xx - Variance-Covariance Matrix of unknowns:")
print (sigmaxx)
print ("--------------------------------------------------------")

## hyp test to test if variances are the same

##sig_level1=0.05
##pop_var1=np.var(
## hyp test to test if it is a sphere
sig_level = 0.05
r_var=float(sigmaxx[3,3])
##r_var=float(np.var(radii))
pop_var=0.000009*3 #from page
df=(len(A)*3)-12
t_stat = (df*(r_var))/(pop_var)
signi= chi2.ppf((1-sig_level),df)

print ("--------------------------------------------------------")
print ("--------------------------------------------------------")
print ("HYPOTHESIS TEST: CHI SQUARED")
print ("H0: pop_var = sample_var")
print ("Ha: pop_var < sample_var")
print ("Test Stat: χ^2 = (dof*sample_var)/pop_var")
print ("Reject H0 if χ^2 > χ^2_(v,α) | else, fail to reject Ho")
print ("--------------------------------------------------------")
print ("--------------------RESULTS TO FOLLOW-------------------")
print ("--------------------------------------------------------")
print ("Test Stat (χ^2): ",t_stat)
print ("Chi Squared Value from table (χ^2_(v,α)): ",signi)

if t_stat > signi:
    print ('RESULT: Reject Null Hypothesis')

else:
    print ('RESULT: Fail to reject Null Hypothesis')

#points showed on graph
##http://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to    
fig=pylab.figure()
ax = Axes3D(fig)
ax.scatter(x_plot,y_plot,z_plot)
pyplot.show()
