

class Observation(object):
    def __init__(self, from_point=None, to_point=None, raw_value=None):
        self.from_point = from_point
        self.to_point = to_point
        self.raw_value = raw_value

class DistanceObservation(Observation):
    def __init__(self, from_point=None, to_point=None, raw_value=None):
        Observation.__init__(self, to_point=to_point, from_point=from_point)

class DirectionObservation(Observation):
    def __init__(self, from_point=None, to_point=None, raw_value=None):
        Observation.__init__(self, to_point=to_point, from_point=from_point)
