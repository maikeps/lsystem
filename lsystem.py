import renderer

class LSystem:

	# A Lindenmayer System consists of:
	# -Axiom
	# -Rules
	# -Order(Level of detail)
	# -Step Length(px)
	# -Left Turning Angle
	# -Right Turning Angle
	# -Randomize Step(%)
	# -Randomize Angle(%)
	def __init__(self, fractal):
		self.rules = fractal['rules']
		self.axiom = fractal['axiom']
		self.turn_angle = fractal['turn_angle']
		self.draw_forward = fractal['draw_forward']
		self.move_forward = fractal['move_forward']
		self.starting_angle = fractal['starting_angle']

		self.renderer = renderer.Renderer(800, 600, 10, self.starting_angle)

	def apply_rule(self, string, recursion_depth):
		if recursion_depth == 0:
			return string

		new_string = ''

		for char in string:
			modification = ''
			for rule in self.rules:
				if char == rule:
					modification = self.rules[rule]

			if modification == '':
				modification = char

			new_string += modification

		return self.apply_rule(new_string, recursion_depth-1)

	def process_string(self, final_string):
		for char in final_string:
			if char in self.draw_forward:
				self.renderer.draw_forward()
			elif char in self.move_forward:
				self.renderer.move_forward()
			elif char == '[':
				self.renderer.stack()
			elif char == ']':
				self.renderer.pop()
			elif char == '+':
				self.renderer.turn_left(self.turn_angle)
			elif char == '-':
				self.renderer.turn_right(self.turn_angle)

		self.renderer.done()


sierpinski = {
	'rules': {'A': '+B-A-B+', 'B': '-A+B+A-'},
	'axiom': 'A',
	'turn_angle': 60,
	'draw_forward': ['A', 'B'],
	'move_forward': [],
	'starting_angle': 0
}

koch = {
	'rules': {'F': 'F+F-F-F+F'},
	'axiom': 'F',
	'turn_angle': 90,
	'draw_forward': ['F'],
	'move_forward': [],
	'starting_angle': 0
}

cantor = {
	'rules': {'A': 'ABA', 'B': 'BBB'},
	'axiom': 'A',
	'turn_angle': 0,
	'draw_forward': ['A'],
	'move_forward': ['B']
}

fractal = {
	'rules': {'F': 'F+F--F+F'},
	'axiom': 'F',
	'turn_angle': 45,
	'draw_forward': ['F'],
	'move_forward': [],
	'starting_angle': 0
}

dragon = {
	'rules': {'X': 'X+YF+', 'Y': '-FX-Y'},
	'axiom': 'FX',
	'turn_angle': 90,
	'draw_forward': ['F'],
	'move_forward': [],
	'starting_angle': 0
}

pythagoras = {
	'rules': {'1': '11', '0': '1[+0]-0'},
	'axiom': '0',
	'turn_angle': 45,
	'draw_forward': ['0', '1'],
	'move_forward': [],
	'starting_angle': 0
}

fractal_plant = {
	'rules': {'X': 'F−[[X]+X]+F[+FX]−X', 'F': 'FF'},
	'axiom': 'X',
	'turn_angle': 20,
	'draw_forward': ['F'],
	'move_forward': [],
	'starting_angle': 0
}

cesaro_koch = {
	'rules': {'F': 'F+F--F+F'},
	'axiom': 'F',
	'turn_angle': 85,
	'draw_forward': ['F'],
	'move_forward': [],
	'starting_angle': 0
}

penrose = {
    'rules': {
    	'F': '',
	    'W': 'YF++ZF----XF[-YF----WF]++',
	    'X': '+YF--ZF[---WF--XF]+',
	    'Y': '-WF++XF[+++YF++ZF]-',
	    'Z': '--YF++++WF[+ZF++++XF]--XF'
    },
	'axiom': '[X]++[X]++[X]++[X]++[X]',
	'turn_angle': 36,
	'draw_forward': ['F'],
	'move_forward': [],
	'starting_angle': 0
}

# f = {
# 	'rules': {},
# 	'axiom': '',
# 	'turn_angle': ,
# 	'draw_forward': [],
#	'move_forward': [],
#	'starting_angle': 0
# }

lsystem = LSystem(penrose)

new_str = lsystem.apply_rule(lsystem.axiom, 2)

lsystem.process_string(new_str)