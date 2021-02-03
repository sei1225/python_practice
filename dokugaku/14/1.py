class Square: 
	square_list = []
	
	def __init__(self,sl):
		self.side_length = sl
		self.square_list.append(sl)
		
square_1 = Square(3)
square_2 = Square(5)
square_3 = Square(7)

print(square_1.square_list)
