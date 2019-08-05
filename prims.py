from collections import deque
import math
import time

INFINITY = float("inf")

class Graph:
	def __init__(self, filename):
		graph_edges = []
		with open(filename) as fhandle:
			li = fhandle.readlines()
			if "U" in li[0]:
				for line in range(1,len(li)):
					edge_from, edge_to, cost, *_ = li[line].strip().split(" ")
					graph_edges.append((edge_from, edge_to, float(cost)))
					graph_edges.append((edge_to,edge_from,float(cost)))		

		self.nodes = set()
		for edge in graph_edges:
			self.nodes.update([edge[0], edge[1]])

		self.edges = graph_edges	
		
	def prim(self, start):
	    visited = {start}
	    nodes,edges = self.nodes,self.edges
	    mst = []

	    while len(visited) != len(self.nodes):
	        possible_edges = (e for e in self.edges if e[0] in visited
	                          and e[1] not in visited)
	        cheapest_edge = min(possible_edges, key=lambda x: x[2])
	        mst.append(cheapest_edge)
	        visited.add(cheapest_edge[1])
	    cost = math.fsum([elem[2] for elem in mst])
       
	    return mst,cost


def main():

	start_0 = time.time()
	verify_algorithm(
		filename="graph.txt",
		start = "A",
		)
	end_0 = time.time()
	time_0 = end_0 - start_0
	print(time_0)

	print("*******************")	
	
	
	start_1 = time.time()
	verify_algorithm(
		filename="large_graph.txt",
		start = "A",
		)
	end_1 = time.time()
	time_1 = end_1 - start_1
	print(time_1)

	print("*******************")	

	
	start_2 = time.time()
	verify_algorithm(
		filename="undir_3.txt",
		start = "A",
		)
	end_2 = time.time()
	time_2 = end_2 - start_2
	print(time_2)	



def verify_algorithm(filename,start):
	
	graph = Graph(filename)
	mst,cost = graph.prim(start)
	print("Minimum Spanning Tree is {} and total min cost is {}".format(mst,cost))
	return
	

if __name__ == "__main__":
	main()