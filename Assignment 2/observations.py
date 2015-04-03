import random


class Observation(object):
    def __init__(self, from_point=None, to_point=None):
        self.from_point = from_point
        self.to_point = to_point

class DistanceObservation(Observation):
    def __init__(self, from_point=None, to_point=None, meters=None):
        Observation.__init__(self, to_point=to_point, from_point=from_point)
        self.meters = meters

class DirectionObservation(Observation):
    def __init__(self, from_point=None, to_point=None, radians=None):
        Observation.__init__(self, to_point=to_point, from_point=from_point)
        self.radians = radians

def add_random_error_to_observation(observation):
    if isinstance(observation, DistanceObservation):
        random_error = random.randint(-100, 100) * 0.01
        observation.meters = observation.meters + random_error
    elif isinstance(observation, DirectionObservation):
        random_error = random.randint(-100, 100) * 0.01
        observation.radians = observation.radians + random_error
    else:
        raise Exception('Unknown tpye of observation')
    return observation

def get_list_of_observations_with_random_errors(list_of_observations=None):
    list_of_errored_observations = []
        for observation in list_of_observations:
            list_of_errored_observations.append(add_random_error_to_observation(observation))
    return list_of_errored_observations
