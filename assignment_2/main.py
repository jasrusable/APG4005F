import math
import numpy
import logging
import random
import utils
import copy
from points import Point
from observations import DistanceObservation, DirectionObservation
from file_stuff import *
from plot import plot_list_of_points


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


points = get_list_of_points_from_file('data/true_points.csv')
observations = get_list_of_observations_from_file('data/true_observations.csv')
tainted_observations = get_list_of_observations_with_random_errors(observations)
write_file_from_list_of_observations(observations, path='data/output_observations')
write_file_from_list_of_observations(tainted_observations, path='data/error_output_observations')
