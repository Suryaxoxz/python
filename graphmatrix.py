class Graph:
	# number of vertices
	n = 0

	# adjacency matrix
	g =[[0 for x in range(10)] for y in range(10)]
	
	# constructor
	def __init__(self, x):
		self.n = x

		# initializing each element of the adjacency matrix to zero
		for i in range(0, self.n):
			for j in range(0, self.n):
				self.g[i][j]= 0

	def displayAdjacencyMatrix(self):
		print("\n\n Adjacency Matrix:", end ="")
		
		# displaying the 2D array
		for i in range(0, self.n):
			print()
			for j in range(0, self.n):
				print("", self.g[i][j], end ="")
	def addEdge(self, x, y):

		# checks if the vertex exists in the graph 
		if(x>= self.n) or (y >= self.n):
			print("Vertex does not exists !")
		
		# checks if the vertex is connecting to itself
		if(x == y):
			print("Same Vertex !")
		else:
			
			# connecting the vertices
			self.g[y][x]= 1
			self.g[x][y]= 1	

	def addVertex(self):
		
		# increasing the number of vertices
		self.n = self.n + 1
		
		# initializing the new elements to 0 
		for i in range(0, self.n):
			self.g[i][self.n-1]= 0
			self.g[self.n-1][i]= 0				
	def removeVertex(self, x):
		
		# checking if the vertex is present
		if(x>self.n):
			print("Vertex not present !")
		else:
		
			# removing the vertex
			while(x<self.n):
		
				# shifting the rows to left side 
				for i in range(0, self.n):
					self.g[i][x]= self.g[i][x + 1]
			
				# shifting the columns upwards
				for i in range(0, self.n):
					self.g[x][i]= self.g[x + 1][i]
				x = x + 1

			# decreasing the number of vertices
			self.n = self.n - 1			


# creating objects of class Graph 
obj = Graph(4)
	
# calling methods
obj.addEdge(0, 1)
obj.addEdge(0, 2)
obj.addEdge(1, 2)
obj.addEdge(2, 3)
# the adjacency matrix created
obj.displayAdjacencyMatrix()

# adding a vertex to the graph
obj.addVertex()
# connecting that vertex to other existing vertices
obj.addEdge(4, 1)
obj.addEdge(4, 3)
# the adjacency matrix with a new vertex
obj.displayAdjacencyMatrix()
	
# removing an existing vertex in the graph
obj.removeVertex(1)
# the adjacency matrix after removing a vertex
obj.displayAdjacencyMatrix()
 