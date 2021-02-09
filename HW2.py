import networkx as nx
import matplotlib.pyplot as plt
import math

def drawGraph(g):
	pos = nx.spring_layout(g)
	plt.figure(figsize=(10,10))
	nx.draw_networkx(g, pos=pos, with_labels=True)
	plt.axis('off')
	plt.show()

#Read in Data from file
DolphinGraph = nx.readwrite.gml.read_gml("dolphins.gml")	


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
	
def EffectiveEccentricity(g):
	print("\n=============== #5 ===============")
	#What is the shortest path length that reaches 90% of all dolphins, from the optimal starting node?
	totalDolphins = len(list(g.nodes))
	dolphinsToKeep = math.floor(totalDolphins * 0.9)

	#Calculate every shortest path for every dolphin
	spaths = dict(nx.all_pairs_shortest_path_length(g))

	#Will hold the length of the longest path it takes for each dolphin to reach 90% of the others
	#To get the effective eccentricity, we'll take the min() from this list and that's the answer.
	longestPaths = list()
	ctr = 0
	
	#Loop through the (ascending) shortest paths to all other dolphins for each dolphin. Append the length of the path it took to reach the 55th dolphin for each dolphin, and then print the minimum value from that list. That number will represent the shortest path possible to reach 90% of all other dolphins (not from any starting point though, the optimal starting point).
	for node1 in spaths:
		ctr = 0
		for node2 in spaths[node1]:
			ctr = ctr+1
			if(ctr == dolphinsToKeep):
				longestPaths.append(spaths[node1][node2])
				break
	

	#Apparently SN100 is the dolphin to start at		
	print("Effective Eccenctricity: ", max(longestPaths))
	
	
def Density(g):
	print("\n=============== #6 ===============")
	N = (len(list(g.nodes)) * len(list(g.nodes))) / 2
	print("Density: ", len(list(g.edges))/N)
	
	
#Driver
DegreeOutput(DolphinGraph)
CharacteristicPathLength(DolphinGraph)
Diameter(DolphinGraph)
CenterAndPeripheral(DolphinGraph)
EffectiveEccentricity(DolphinGraph)
Density(DolphinGraph)

drawGraph(DolphinGraph)









