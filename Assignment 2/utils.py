import math


def to_dms(value, format_='rad', delim='.'):
    dms = math.degrees(value)
    if format_ == 'rad':
        pass
    elif format_ == 'deg':
        pass
    else:
        raise Exception('Unknown format_ {0}'.format(format_))

def to_radians(value, current_format_, delim):
    if not value:
        raise Exception('No value to convert to radians.')
    if current_format_ == 'dms':
        dms = value.split(delim)
        deg = float(dms[0])
        min_ = float(dms[1])
        sec = float(dms[2])
        if deg < 0:
            radians = math.radians(-(abs(deg) + (min_ / 60) + (sec / 3600)))
        else:
        	radians = math.radians(deg + (min_ / 60) + (sec / 3600))
    elif current_format_ == 'deg':
        radians =  math.radians(value)
    else:
        raise Exception('Unknown current_format_ {0}'.format(current_format_))
    return radians
