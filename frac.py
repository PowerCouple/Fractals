import turtle
import math

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
	
def drawLines(line_arr):
	turt = turtle.Turtle()
	turtle.shape("blank")
	#draws each line in the line_arr
	for line in line_arr:
		draw_single_line(line,turt)
	turtle.done()

def iteration(line_arr):
	#does the next iteration of the fractal
	arr = []
	for line in line_arr:
		start_point = line.start
		end_point = line.end
		p1 = Point((2*start_point.x+end_point.x)/3.,(2*start_point.y+end_point.y)/3.)
		p2 = getPoint(line)
		p3 = Point((start_point.x+2*end_point.x)/3.,(start_point.y+2*end_point.y)/3.)

		arr.append(Line(start_point,p1))
		arr.append(Line(p1,p2))
		arr.append(Line(p2,p3))
		arr.append(Line(p3,end_point))

	return arr


def getPoint(line):
	sx = line.start.x
	sy = line.start.y
	fx = line.end.x
	fy = line.end.y

	if (fx==sx):
		if (fy==sy):
			print "error"
		elif (fy < sy):
			theta = -math.pi/2
		else:
			theta = math.pi/2
	else:
		theta = math.atan((fy-sy)/(fx-sx))
		if (fx < sx):
			theta += math.pi

	length = math.sqrt((sx-fx)**2+(sy-fy)**2)

	x = 1./2
	y  = 1./(2*math.sqrt(3))

	return Point(length*(x*math.cos(theta)-y*math.sin(theta))+sx,length*(x*math.sin(theta)+y*math.cos(theta))+sy)



def main():
	turtle.shape("blank")
	p1 = Point(0,0)
	p2 = Point(100,0)
	p3 = Point(50,50*math.sqrt(3))
	l1 = Line(p1,p3)
	l2 = Line(p3,p2)
	l3 = Line(p2,p1)
	prev = [l1,l2,l3]
	for i in range (0,5):
		prev = iteration(prev)

	drawLines(prev)


if __name__ == "__main__":
	main()


s = Point(0,0)
f = Point(1,0)
l = Line(s,f)
