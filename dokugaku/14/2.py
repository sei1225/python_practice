class Square:
	def __init__(self,sl):
		self.side_length = sl
		
	def __repr__(self):
		return '{}by'.format(self.side_length)*4
		
sqare_1 = Square(5)
print(sqare_1)
