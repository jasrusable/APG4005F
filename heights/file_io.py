from points import Point
from observations import Observation
from utils import to_radians, get_point_by_name


def read_points(filepath='points.txt', delim=','):
	points = list()
	with open (filepath, 'r') as f:
		for line in f:
			if line.startswith('#'):
				continue
			line = line.strip('\n')
			line_parts = line.split(delim)
			name = line_parts[0].strip(' ')
			type_ = line_parts[1].strip(' ')
			x = float(line_parts[2])
			y = float(line_parts[3])
			z = float(line_parts[4])
			points.append(Point(name, type_, x, y, z))
	return points

def read_observations(type_, known_points, filepath='obs.txt', delim=','):
	assert(type_ in ['distance', 'direction', 'height'])
	observations = list()
	known_point_names = list()
	for point in known_points:
		known_point_names.append(point.name)
	with open(filepath, 'r') as f:
		for line in f:
			if line.startswith('#'):
				continue
			line = line.strip('\n')
			line_parts = line.split(delim)
			from_name = line_parts[0].strip(' ')
			if from_name not in known_point_names:
				raise Exception("From point {0} not defined in known_points.".format(from_name))
			from_ = get_point_by_name(from_name, known_points)
			to_name = line_parts[1].strip(' ')
			if to_name not in known_point_names:
				raise Exception("To point '{0}'' not defined in known_points.".format(to_name))
			to = get_point_by_name(to_name, known_points)
			value = line_parts[2].strip(' ')
			if type_ == 'direction':
				value = to_radians(value, current_format='dms', delim='.')
			observations.append(Observation(from_, to, type_, value))
	return observations
