import networkx as nx
import matplotlib.pyplot as plt


def drawGraph(g):
	pos = nx.spring_layout(g)
	plt.figure(figsize=(10,10))
	nx.draw_networkx(g, pos=pos, with_labels=True)
	plt.axis('off')
	plt.show()

#Read in Data from file
DolphinGraph = nx.readwrite.gml.read_gml("dolphins.gml")	
#drawGraph(DolphinGraph)

#(1) Output Degree Stats
def DegreeOutput(g):
	#Init
	for node in g:	
		minDegree = g.degree[node]
		maxDegree = g.degree[node]
		degreeSum = 0
		break
	
	
	for node in g:
		if(g.degree[node] < minDegree):
			minDegree = g.degree[node]
		if(g.degree[node] > maxDegree):
			maxDegree = g.degree[node]
			
		degreeSum += g.degree[node]
	
	print("=============== #1 ===============")
	print("Max Degree: ", maxDegree)
	print("Min Degree: ", minDegree)
	print("Average Degree: ", degreeSum/len(g.nodes))
	
	
	
def CharacteristicPathLength(g):
	print("\n=============== #2 ===============")
	print("Average Shortest Path Length: ", nx.average_shortest_path_length(g))
	
def Diameter(g):
	print("\n=============== #3 ===============")
	print("Diameter: ", nx.diameter(g))
	
def CenterAndPeripheral(g):
	print("\n=============== #4 ===============")
	print("Center Nodes: ", nx.center(g))
	print("Peripheral Nodes: ", nx.periphery(g))
	
DegreeOutput(DolphinGraph)
CharacteristicPathLength(DolphinGraph)
Diameter(DolphinGraph)
CenterAndPeripheral(DolphinGraph)
