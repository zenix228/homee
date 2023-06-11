class KgToPounds:
	def __init__(self, kg):
		self.kg = kg

	def to_pounds(self):
		return self.kg * 2.20462

	def set_kg(self, kg):
		self.kg = kg

	def get_kg(self):
		return self.kg