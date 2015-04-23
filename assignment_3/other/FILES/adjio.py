
def readInfo(pointfile, obsfile, freenet):
    pfile = open(pointfile, 'r')
    ofile = open(obsfile,'r')
    free  = open(freenet, 'r')
    point = {}


    # read points
    for line in pfile:
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
        
##    for line in free:
##        s = line.split(',')
##
##        name = sp[0].strip()
##        x = float(sp[1])
##        y = float(sp[2])
##        status = int(sp[3])
##
##        coord = [x, y]
##        info = {}
##        info['Name'] = name
##        info['Coord'] = coord
##
##        
##        info['Status'] = status
##        
##        points[name] = info

    # get the unknowns
    unkset = set()

    for name, p in point.items():
        if p['Status'] == 0:
            unkset.add(name + "_x")
            unkset.add(name + "_y")

    unklst = list(unkset)
    unklst.sort()

    # get unknowns free
    unksets = set()
    for name, p in point.items():      
        unksets.add(name + "_x")
        unksets.add(name + "_y")

    unklsts = list(unksets)
    unklsts.sort()

    

    # get observations
    obs =[]
    for observ in ofile:
        observ = observ.rstrip('\n')
        sp = observ.split(',')
        sta = sp[0]
        targ = sp[1]
        obs += [{'station':sta,'target':targ,'obser':sp[2]}]

        
    return point, unklst, obs,unklsts
