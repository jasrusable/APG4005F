import math


def to_radians(value, current_format, delim):
    if current_format == 'dms':
        dms = value.split(delim)
        deg = float(dms[0])
        min_ = float(dms[1])
        sec = float(dms[2])
        if deg < 0:
            radians = math.radians(-(abs(deg) + (min_ / 60) + (sec / 3600)))
        else:
        	radians = math.radians(deg + (min_ / 60) + (sec / 3600))
    elif current_format == 'dd':
        radians =  math.radians(value)
    else:
        raise Exception('Unknown current_format {0}'.format(current_format))
    return radians

def get_point_by_name(name, points):
    matched_points = list()
    for point in points:
        if point.name == name:
            matched_points.append(point)
    assert(len(matched_points) == 1)
    return matched_points[0]