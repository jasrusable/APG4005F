import math


def to_radians(value, format_='deg', delim=':'):
    if not value:
        raise Exception('No value to convert to radians.')
    if format_ == 'dms':
        dms = value.split(delim)
        deg = float(dms[0])
        min_ = float(dms[1])
        sec = float(dms[2])
        if deg < 0:
            radians = math.radians(-(abs(deg) + (min_ / 60) + (sec / 3600)))
        else:
        	radians = math.radians(deg + (min_ / 60) + (sec / 3600))
    elif format_ == 'deg':
        radians =  math.radians(value)
    else:
        raise Exception('Unknown format {0}'.format(format_))
    return radians
