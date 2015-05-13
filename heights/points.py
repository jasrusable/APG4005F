class Point(object):
	def __init__(self, name, type_, x, y, z):
		self.name = name
		self.type_ = type_
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return "<Point name={name}, type={type_}, x={x}, y={y}, z={z}".format(
			name=self.name,
			type_=self.type_,
			x=self.x,
			y=self.y,
			z=self.z,
		)
