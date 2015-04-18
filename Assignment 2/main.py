import math
import numpy
import logging
import random
import utils
from points import Point
from observations import DistanceObservation, DirectionObservation
from file_stuff import *
from plot import plot_list_of_points


logger = logging.getLogger(__name__)


def add_random_error_to_direction_observation(direction_observation):
    if isinstance(direction_observation, DirectionObservation):
        random_error = random.randint(-100, 100) * 0.01
        observation.radians = observation.radians + random_error
    else:
        raise Exception('type of observation is not DirectionObservation')
    return observation

def add_random_error_to_distance_observation(distance_observation):
    if isinstance(distance_observation, DistanceObservation):
        random_error = random.randint(-100, 100) * 0.05
        observation.meters = observation.meters + random_error
    else:
        raise Exception('type of observation is not DistanceObservation')
    return observation

def get_list_of_observations_with_random_errors(list_of_observations=None):
    list_of_errored_observations = []
    for observation in list_of_observations:
        if isinstance(observation, DirectionObservation):
            list_of_errored_observations.append(add_random_error_to_direction_observation(observation))
        elif isinstance(observation, DistanceObservation):
            list_of_errored_observations.append(add_random_error_to_distance_observation(observation))
    return list_of_errored_observations


def write_pseudo_observations_to_file(points, path='observations.csv'):
    for from_point in points:
        for to_point in points:
            if to_point != from_point:
                pass


points = get_list_of_points_from_file('true_points.csv')
observations = get_list_of_observations_from_file('true_observations.csv')
