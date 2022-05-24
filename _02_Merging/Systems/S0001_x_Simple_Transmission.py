# S0001_x_Simple_Transmission.py


# Code:
class S0001_x_Simple_Transmission:
	def __init__(self):
		# --------------------------------------------------
		#            Definitions of variables
		# --------------------------------------------------
		self.x = [{}, {}, {}, {}, {}, {}]  # Design variables
		self.y = [{}, {}, {}, {}, {}, {}, {}]  # Quantities of interest
		self.p = [{}, {}, {}]
		self.index = {}
		self.samples = {{}}
		
		# --------------------------------------------------
		#            Input variables
		# --------------------------------------------------
		self.sampleSize = 0  # Number of samples
		self.diagram = []  # Diagram list
		
		self.m = 0  # Number of quantities of interest
		self.d = 0  # Number of design variables
		self.np = 0  # Number of parameters
		self.k = 0  # necessary for plot_m_x
		self.b = 0  # necessary for writeInputOutput
		
		self.good_design_color = 'green'  # Color of good designs
		
		# Line definition for solution spaces
		self.solutionspace_line_color = 'black'
		self.solutionspace_line_width = 2
		self.solutionspace_line_type = '--'
		
		self.legend = ''  # Legend text
		
		self.save_as = 'S0001_s_Simple_Transmission.py'  # Filename of saved file

	# --------------------------------------------------
	#            Functions
	# --------------------------------------------------
	def S0001_x_Simple_Transmission(self):
		# Try to load saved data
		self.sampleSize = 3000

		self.diagram = [1, 2]  # Choosing variables to be shown in the diagrams

		# Design Variables
		design_variables = [
			['z_{11}', '-', 0, 100],
			['z_{12}', '-', 0, 100],
			['z_{21}', '-', 0, 100],
			['z_{22}', '-', 0, 100],
			['n_{in}', '-', 0, 100],
			['T_{in}', '-', 0, 100]
		]

		# Design variables 2
		for i in range(0, len(design_variables)):
			self.x[i]["name"] = design_variables[i][0]
			self.x[i]["unit"] = design_variables[i][1]
			self.x[i]["dsl"] = design_variables[i][2]
			self.x[i]["dsu"] = design_variables[i][3]
			self.x[i]["l"] = design_variables[i][2]
			self.x[i]["u"] = design_variables[i][3]

		# Quantities of interest
		quantities_of_interest = [
			['T_{out}', '-', [0, 0, 1], 0, 200, 1],
			['n_{out}', '-', [0, 0, 1], 0, 200, 1],
		]

		# Quantities of interest 2
		for i in range(0, len(quantities_of_interest)):
			self.y[i]["name"] = quantities_of_interest[i][0]
			self.y[i]["unit"] = quantities_of_interest[i][1]
			self.y[i]["color"] = quantities_of_interest[i][2]
			self.y[i]["l"] = quantities_of_interest[i][3]
			self.y[i]["u"] = quantities_of_interest[i][4]
			self.y[i]["active"] = quantities_of_interest[i][5]
			self.y[i]["condition"] = 'Violating ' + quantities_of_interest[i][0]

		# Parameters
		parameters = [
			# Text parameters %'Name','Unit',15.6
		]

		# Parameters 2
		for i in range(0, len(parameters)):
			self.p[i]["name"] = parameters[i][0]
			self.p[i]["unit"] = parameters[i][1]
			self.p[i]["value"] = parameters[i][2]

		# Marker size of samples
		self.samples["marker"]["size"] = 10
		self.samples["marker"]["type"] = "."
		self.m = len(self.y)
		self.d = len(self.x)
		self.np = len(self.p)

		self.legend = self.CreateLegend(self.y)  # Legende erstellen vereinfacht durch Steger

		self.k = 0
		self.b = 0

	# Calculates system response
	def SystemResponse(self, x):
		# Importing modules
		from _02_Merging.Systems.S0001_f_Simple_Transmission import S0001_f_Simple_Transmission

		# Function:
		y = [[], []]
		[y[0], y[1]] = S0001_f_Simple_Transmission(x[0], x[1], x[2], x[3], x[4], x[5])
		return y

	def CreateLegend(self, y):
		legend = ["{\color{green} \ bullet }Good design"]
		for i in range(0,self.m):
			if self.y[i]["active"] == 1:
				legend.append("{\color[rgb]{" + self.y[i]["color"] + "]} \ bullet }" + self.y[i]["condition"])
		return legend
























