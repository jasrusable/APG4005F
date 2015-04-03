from random import randint
import math
import numpy
import logging
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from points import Point
from observations import DistanceObservation, DirectionObservation


logger = logging.getLogger(__name__)


def plot_list_of_points(list_of_points):
    x, y, z = [], [], []
    for point in list_of_points:
        x.append(point.x)
        y.append(point.y)
        z.append(point.z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

class PseudoObservation(object):
    def __init__(self, from_point=None, to_point=None, direction=None, distance=None):
        pass

def write_pseudo_observations_to_file(points, path='observations.csv'):
    for from_point in points:
        for to_point in points:
            if to_point != from_point:
                pass

def generate_file_from_list_of_points(list_of_points=None, path='output_file.csv'):
    f = open(path, 'w')
    for point in list_of_points:
        x = point.x
        y = point.y
        z = point.z
        line = str(x) + ", " + str(y) + ", " + str(z) + "\n"
        f.write(line)
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

def get_lists_of_observations_from_file(path='observations.csv', delim=','):
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
            dir_obs = DirectionObservation(from_point=from_point, to_point=to_point, value=value)
            list_of_direction_observations.append(dir_obs)
        if distance:
            dist_obs = DistanceObservation(from_point=from_point, to_point=to_point, value=value)
            list_of_distance_observations.append(dist_obs)



list_of_points = get_list_of_points_from_file('points.csv')
plot_list_of_points(list_of_points)
