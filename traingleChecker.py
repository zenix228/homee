class TriangleChecker:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def is_triangle(self):
		if self.a <= 0 or self.b <= 0 or self.c <= 0:
			return "С отрицательными числами ничего не выйдет!"
		elif not (isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.c,(int, float))):
			return "Нужно вводить только числа!"
		elif self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
			return "Жаль, но из этого треугольник не сделать."
		else:
			return "Ура, можно построить треугольник!"