import math
import numpy
import logging
import random
import utils
import copy
from points import Point
from observations import DistanceObservation, DirectionObservation
from file_io import *
from plot import plot_list_of_points
import scipy.linalg as LA


logger = logging.getLogger(__name__)


def add_random_error_to_direction_observation(direction_observation):
    direction_observation = copy.copy(direction_observation)
    random_error = random.randint(-100, 100) * 0.000001
    direction_observation.radians = direction_observation.radians + random_error        
    return direction_observation

def add_random_error_to_distance_observation(distance_observation):
    distance_observation = copy.copy(distance_observation)
    random_error = random.randint(-100, 100) * 0.001
    distance_observation.meters = distance_observation.meters + random_error
    return distance_observation

def get_list_of_observations_with_random_errors(list_of_observations):
    list_of_errored_observations = []
    for observation in list_of_observations:
        if isinstance(observation, DirectionObservation):
            list_of_errored_observations.append(add_random_error_to_direction_observation(observation))
        elif isinstance(observation, DistanceObservation):
            list_of_errored_observations.append(add_random_error_to_distance_observation(observation))
        else:
            raise Exception('Unknown observation type {0}: '.format(type(observation)))
    return list_of_errored_observations


parametric_points = get_list_of_points_from_file('data/raw_parametric_points.csv')
free_points = get_list_of_points_from_file('data/raw_free_points.csv')
observations = get_list_of_observations_from_file('data/raw_observations.csv')

def get_distance(coordinate1, coordinate2):
    delta_y = coordinate2.y - coordinate1.y
    delta_x = coordinate2.x - coordinate1.x
    return math.sqrt((delta_y**2) + (delta_x**2))

def get_direction(coordinate1, coordinate2):
    delta_y = coordinate2.y - coordinate1.y
    delta_x = coordinate2.x - coordinate1.x
    direction = math.atan2(delta_y,delta_x)
    if delta_x < 0 and delta_y > 0:
        direction = direction 

    elif delta_x < 0 and delta_y < 0:
        direction = direction + math.pi

    elif delta_x > 0 and delta_y < 0:
        direction = direction + 2*math.pi

    return direction

def get_point_by_name(name, points):
    wanted_point = None
    for point in points:
        if name == point.name:
            wanted_point = point
    if not wanted_point:
        raise Exception('Point {0} not found.'.format(name))
    return wanted_point

def get_provisional_points(points):
    provisional_points = []
    for point in points:
        if point.type_ == 'P':
            provisional_points.append(point)
    return provisional_points



def solve_parametric(observations, points):
    A = numpy.matrix([
        [0,0,0,0],
    ])
    A = numpy.delete(A, (0), axis=0)
    L = numpy.matrix([
        [0],
    ])
    L = numpy.delete(L, (0), axis=0)
    for observation in observations:
        A_row = [0] * len(get_provisional_points(points)) * 2
        L_row = [0]
        to_point = get_point_by_name(observation.to_point_name, points)
        from_point = get_point_by_name(observation.from_point_name, points)
        if isinstance(observation, DirectionObservation):
            observed = observation.radians
            calculated = get_direction(from_point, to_point)
            L_row = [observed - calculated]
            i = 0
            for unknown_point in get_provisional_points(points):
                d = get_distance(to_point, from_point)
                y = -(to_point.x - from_point.x) / d**2
                x = (to_point.y - from_point.y) / d**2
                if to_point == unknown_point:
                    A_row[i] = y
                    A_row[i+1] = x
                elif from_point == unknown_point:
                    A_row[i] = y
                    A_row[i+1] = x
                else:
                    pass
                i += 2
            A = numpy.vstack([A, A_row])
            L = numpy.vstack([L, L_row])

    return A, L


pA, pL = solve_parametric(observations, parametric_points)
pX = (pA.T*pA).I * pA.T * pL
for i in range(3):
    pA, pL = solve_parametric(observations, parametric_points)
    pX = (pA.T*pA).I * pA.T * pL

def solve_free(observations, points):
    A = numpy.matrix([
        [0,0,0,0,0,0,0,0,0,0,0,0],
    ])
    A = numpy.delete(A, (0), axis=0)
    L = numpy.matrix([
        [0],
    ])
    L = numpy.delete(L, (0), axis=0)
    for observation in observations:
        A_row = [0] * len(get_provisional_points(points)) * 2
        L_row = [0]
        to_point = get_point_by_name(observation.to_point_name, points)
        from_point = get_point_by_name(observation.from_point_name, points)
        if isinstance(observation, DirectionObservation):
            observed = observation.radians
            calculated = get_direction(from_point, to_point)
            L_row = [observed - calculated]
            i = 0
            for unknown_point in get_provisional_points(points):
                d = get_distance(to_point, from_point)
                y = -(to_point.x - from_point.x) / d**2
                x = (to_point.y - from_point.y) / d**2
                if to_point == unknown_point:
                    A_row[i] = y
                    A_row[i+1] = x
                elif from_point == unknown_point:
                    A_row[i] = y
                    A_row[i+1] = x
                else:
                    pass
                i += 2
            A = numpy.vstack([A, A_row])
            L = numpy.vstack([L, L_row])

    return A, L
fA, fL = solve_free(observations, free_points)
fATPA = fA.T*fA



def get_G(ATPA):
    eigs = LA.eigh(fATPA)
    temp = []
    for eigen_value, eigen_vector in zip(eigs[0], eigs[1]):
        if round(eigen_value, 3) == 0.0:
            temp.append(eigen_vector)
    return numpy.matrix(temp)
print(numpy.linalg.matrix_rank(fN))
fG = get_G(fATPA)
fN = fA.T*fA + fG*fG.T
        
