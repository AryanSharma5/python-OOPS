# There are many in-built methods : (FOR ARITHMETIC OPERATORS)

# addition       : __add__
# subtract       : __sub__	
# multiplication : __mul__
# True division  : __truediv__
# floor division : __floordiv__
# mod            : __mod__
# power          : __pow__
# left Shift     : __lshift__
# Right Shift    : __rshift__
# and            : __and__
# or             : __or__
# invert         : __invert__
# xor            : __xor__

# For Comparision Operators :

# Less than                : __lt__
# Less than Equal to       : __le__
# Greater than             : __gt__
# Greater than or Equal to : __ge__
# Equal TO                 : __eq__
# Not Equal To             : __ne__


class Points:
	def __init__(self,x,y):
		self.X = x
		self.Y = y

	# without __add__ there will be an error
	def __add__(self, other):
		x = self.X + other.X
		y = self.Y + other.Y
		return x,y

p1 = Points(10,20)
p2 = Points(5,10)

print(p1 + p2)