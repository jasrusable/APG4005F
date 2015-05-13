class Observation(object):
	def __init__(self, from_, to, type_, value):
		self.from_ = from_
		self.to = to
		self.value = value
		self.type_ = type_
	
	def __repr__(self):
		return "<Observation to={to}, from={from_}, type={type}>".format(
			to=self.to,
			from_=self.from_,
			type=self.type_,
		)
