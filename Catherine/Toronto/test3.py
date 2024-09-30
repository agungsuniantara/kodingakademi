# buka folder terminal Toronto
# ketik python3 -m doctest -v test3.py

def right_triangle(side1, side2, hypotenuse):
	"""
	:param side1: float
	:param side2: float
	:param hypotenuse: float

	>>> right_triangle(4,3,5)
	True

	>>> right_triangle(1,1,2)
	False
	"""

	if side1 ** 2 + side2 ** 2 == hypotenuse ** 2:
		return True
	else:
		return False