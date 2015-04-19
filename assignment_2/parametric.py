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


logger = logging.getLogger(__name__)


points = get_list_of_points_from_file('data/true_points.csv')
observations = get_list_of_observations_from_file('data/error_output_observations.csv')
