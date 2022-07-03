# S0002_x_Simple_Transmission.py


# Code:
class S0002_x_Simple_Transmission:
	
	# --------------------------------------------------
	#            Definitions of variables
	# --------------------------------------------------
	x = [{}, {}, {}, {}, {}, {}]  # Design variables
	y = [{}, {}]  # Quantities of interest
	p = []
	index = {}
	samples = {"marker": {}}
	
	# --------------------------------------------------
	#            Input variables
	# --------------------------------------------------
	sampleSize = 0  # Number of samples
	diagram = []  # Diagram list
	
	m = 0  # Number of quantities of interest
	d = 0  # Number of design variables
	np = 0  # Number of parameters
	k = 0  # necessary for plot_m_x
	b = 0  # necessary for writeInputOutput
	
	good_design_color = 'green'  # Color of good designs
	
	# Line definition for solution spaces
	solutionspace_line_color = 'black'
	solutionspace_line_width = 2
	solutionspace_line_type = '--'
	
	legend = ''  # Legend text
	
	save_as = 'S0002_s_Simple_Transmission.py'  # Filename of saved file
	
	# --------------------------------------------------
	#            Functions
	# --------------------------------------------------
	def __init__(self):
		self.sampleSize = 300
		
		self.diagram = [1, 2]  # Choosing variables to be shown in the diagrams
		
		# Design Variables
		design_variables = [
			['z_22', '-',  0, 100],
			['z_21', '-',  0, 100],
			['z_11', '-',  0, 100],
			['z_12', '-',  0, 100],
			['n_in', '-',  0, 100],
			['T_in', '-',  0, 100]
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
			['T_out', '-', [1, 0, 0],  0, 200, 1],
			['n_out', '-', [1, 0, 0],  0, 200, 1]
		]
		
		# Quantities of interest 2
		for i in range(0, len(quantities_of_interest)):
			self.y[i]["name"] = quantities_of_interest[i][0]
			self.y[i]["unit"] = quantities_of_interest[i][1]
			self.y[i]["color"] = quantities_of_interest[i][2]
			self.y[i]["l"] = quantities_of_interest[i][3]
			self.y[i]["u"] = quantities_of_interest[i][4]
			self.y[i]["active"] = quantities_of_interest[i][5]
			self.y[i]["condition"] = "Violating " + quantities_of_interest[i][0]
		
		# Parameters
		parameters = [
			# Text parameters %'Name','Unit',15.6
		]
		self.p = []
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
		from _02_Merging.Systems.S0002_f_Simple_Transmission import S0002_f_Simple_Transmission
		
		# Function:
		y = [[], []]
		[y[0], y[1]] = S0002_f_Simple_Transmission(x[0], x[1], x[2], x[3], x[4], x[5])
		return y
	
	def CreateLegend(self, y):
		legend = ["{\color{green} \ bullet }Good design"]
		for i in range(0, self.m):
			if self.y[i]["active"] == 1:
				legend.append("{\color[rgb]{" + str(self.y[i]["color"]) + "]} \ bullet }" + str(self.y[i]["condition"]))
		return legend
		