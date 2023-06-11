from soda import Soda
from traingleChecker import TriangleChecker
from kg import KgToPounds

shape_2 = TriangleChecker(a=5,b=4,c=4)
print(shape_2.is_triangle())

shape_3 = KgToPounds(kg=100)
print(shape_3.to_pounds())