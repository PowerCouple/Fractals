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

def draw_single_line(line,turt):
	#draws one line
	turt.up()
	turt.setpos(line.start.x, line.start.y)
	turt.down()
	turt.setpos(line.end.x, line.end.y)
	
def draw_lines(line_arr):
	turt = turtle.Turtle()
	turtle.shape("blank")
	#draws each line in the line_arr
	for line in line_arr:
		draw_single_line(line,turt)
	turtle.done()

def iteration(line_arr):
	#does the next iteration of the fractal
	print "iteration"

def main():
	turtle.shape("blank")
	#number of times you want the image to iterate
	it = 5
	num = 100
	p1 = Point(0,0)
	p2 = Point(0,num)
	p3 = Point(num,num)
	p4 = Point(num,0)
	l1 = Line(p1,p2)
	l2 = Line(p2,p3)
	l3 = Line(p3,p4)
	l4 = Line(p4,p1)
	line_arr = [l1,l2,l3,l4]
	draw_lines(line_arr)


if __name__ == "__main__":
	main()
