import networkx as nx
import matplotlib.pyplot as plt


G = nx.readwrite.gml.read_gml("dolphins.gml")

def drawGraph(g):
	pos = nx.spring_layout(g)
	plt.figure(figsize=(10,10))
	nx.draw_networkx(g, pos=pos, with_labels=True)
	plt.axis('off')
	plt.show()
	
	
drawGraph(G)
