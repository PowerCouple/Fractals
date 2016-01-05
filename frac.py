import turtle

class Line:
	def __init__(self, my_start, my_end):
		self.start = my_start
		self.end = my_end
	
	def __str__(self):
		return "[" + str(self.start) + "," + str(self.end) + "]"

class Point:
	def __init__(self, my_x, my_y):
		self.x = my_x
		self.y = my_y
	
	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"
	
def iteration(line_arr):
	#does the next iteration of the fractal
	print "iteration"

def main():
	print "hello"
	#number of times you want the image to iterate
	it = 5
	p1 = Point(0,0)
	print p1
	p2 = Point(0,1)
	print p2
	l1 = Line(p1,p2)
	print l1	

if __name__ == "__main__":
	main()
