import tkinter
import math

class Renderer:

	def __init__(self, width, height, line_length, starting_angle):
		self.master = tkinter.Tk()
		self.canvas = tkinter.Canvas(width=width, height=height)
		self.canvas.pack()

		self.line_length = line_length

		# initialize renderer position and angle
		self.draw_x = width/2
		self.draw_y = height/2

		# Angle starts at 90 degrees (up)
		self.angle = starting_angle

		self.position_stack = []
		self.angle_stack = []

	def draw_forward(self):
		start_x = self.draw_x
		start_y = self.draw_y

		self.move_forward()

		self.canvas.create_line(start_x, start_y, self.draw_x, self.draw_y)

	def move_forward(self):
		self.draw_x = self.draw_x + math.cos(math.radians(self.angle)) * self.line_length
		self.draw_y = self.draw_y - math.sin(math.radians(self.angle)) * self.line_length

	def turn_left(self, degrees):
		self.angle = (self.angle + degrees) % 360

	def turn_right(self, degrees):
		self.angle = (self.angle - degrees) % 360

	def done(self):
		self.master.mainloop()

	def stack(self):
		self.position_stack.append((self.draw_x, self.draw_y))
		self.angle_stack.append(self.angle)

	def pop(self):
		self.draw_x = self.position_stack[-1][0]
		self.draw_y = self.position_stack[-1][1]
		self.angle = self.angle_stack[-1]

		del self.position_stack[-1]
		del self.angle_stack[-1]