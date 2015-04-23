import numpy as np

file = open('points.csv', 'r')
f=open('OBSERVATIONS.csv','r')

point = {}
for line in file:
    sp = line.split(',')

    name = sp[0].strip()
    x = float(sp[1])
    y = float(sp[2])
    status = int(sp[3])

    coord = [x, y]
    info = {}
    info['Name'] = name
    info['Coord'] = coord
    info['Status'] = status
    
    point[name] = info
    

unkset = set()
for name, p in point.items():
    if p['Status'] == 0:
        unkset.add(name + "_x")
        unkset.add(name + "_y")

unklst = list(unkset)
unklst.sort()

print(unklst)
print()
obs1=[]
for observ in f:
    observ=observ.rstrip('\n')
    sp=observ.split(',')
    sta=sp[0]
    targ=sp[1]
    obs1+=[{'station':sta,'target':targ,'obser':sp[2]}]
print(obs1)
obs = [{'p0': 'Q', 'p1': 'B', 'obs': 25.2},
       {'p0': 'C', 'p1': 'P', 'obs': 52.2},
       {'p0': 'Q', 'p1': 'C', 'obs': 72.2}]

lstA = []
for o in obs:
    p0 = point[o['p0']]
    p1 = point[o['p1']]


    dp0x = 5
    dp0y = 7
    dp1x = 12
    dp1y = 45

    rowA = [0.0] * len(unklst)

    if(p0['Status'] == 0):
        index = unklst.index(p0['Name']+'_x')
        rowA[index] = dp0x
        index = unklst.index(p0['Name']+'_y')
        rowA[index] = dp0y

    if(p1['Status'] == 0):
        index = unklst.index(p1['Name']+'_x')
        rowA[index] = dp1x
        index = unklst.index(p1['Name']+'_y')
        rowA[index] = dp1y

    lstA += [rowA]

matA = np.matrix(lstA)

#print(lstA)

##for u, v in zip(unklst, rowA):
##    print(u, v)

