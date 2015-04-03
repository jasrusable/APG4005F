from points import Point
from observations import DistanceObservation, DirectionObservation


def generate_file_from_list_of_points(list_of_points=None, path='output_file.csv', delim=','):
    f = open(path, 'w')
    for point in list_of_points:
        f.write(delim.join([str(point.x), str(point.y), str(point.z)]) + "\n")
    f.close()

def get_list_of_points_from_file(path='points.csv', delim=','):
    f = open(path, 'r')
    list_of_points = []
    for line in f.readlines():
        line = line.strip('\n')
        parts = line.split(delim)
        type_ = parts[0].strip(' ')
        name = parts[1]
        x = parts[2].strip(' ')
        y = parts[3].strip(' ')
        if type_ not in ['CP', 'P']:
            raise Exception('Points type_ is not P nor CP')
        z = 0
        list_of_points.append(
            Point(type_=type_, name=name, x=x, y=y, z=z)
        )
    return list_of_points

def get_list_of_observations_from_file(path='observations.csv', delim=','):
    f = open(path, 'r')
    list_of_direction_observations = []
    list_of_distance_observations = []
    for line in f.readlines():
        line = line.strip('\n')
        parts = line.split(delim)
        type_ = parts[0]
        from_point = parts[1]
        to_point = parts[2]
        direction = parts[3]
        distance = parts[4]
        if direction:
            dir_obs = DirectionObservation(from_point=from_point, to_point=to_point, raw_value=direction)
            list_of_direction_observations.append(dir_obs)
        if distance:
            dist_obs = DistanceObservation(from_point=from_point, to_point=to_point, raw_value=distance)
            list_of_distance_observations.append(dist_obs)
