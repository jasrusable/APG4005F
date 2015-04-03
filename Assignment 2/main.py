import math
import numpy
import logging

from random import randint

from points import Point
from observations import DistanceObservation, DirectionObservation
from file import get_list_of_points_from_file, get_list_of_observations_from_file
from plot import plot_list_of_points


logger = logging.getLogger(__name__)


class PseudoObservation(object):
    def __init__(self, from_point=None, to_point=None, direction=None, distance=None):
        pass

def write_pseudo_observations_to_file(points, path='observations.csv'):
    for from_point in points:
        for to_point in points:
            if to_point != from_point:
                pass


points = get_list_of_points_from_file('points.csv')
observations = get_list_of_observations_from_file('observations.csv')
