from collections import deque
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
					
			else:
				for line in range(1,len(li)):
					edge_from, edge_to, cost, *_ = li[line].strip().split(" ")
					graph_edges.append((edge_from, edge_to, float(cost)))

		self.nodes = set()
		for edge in graph_edges:
			self.nodes.update([edge[0], edge[1]])

		self.adjacency_list = {node: set() for node in self.nodes}
		for edge in graph_edges:
			self.adjacency_list[edge[0]].add((edge[1], edge[2]))

	def shortest_path(self, start_node, end_node):
		unvisited_nodes = self.nodes.copy()  

	   
		distance_from_start = {
			node: (0 if node == start_node else INFINITY) for node in self.nodes
		}
		previous_node = {node: None for node in self.nodes}
		
		while unvisited_nodes:
			current_node = min(
				unvisited_nodes, key=lambda node: distance_from_start[node]
			)
			unvisited_nodes.remove(current_node)

			if distance_from_start[current_node] == INFINITY:
				break
			
			for neighbor, distance in self.adjacency_list[current_node]:
				new_path = distance_from_start[current_node] + distance
				if new_path < distance_from_start[neighbor]:
					distance_from_start[neighbor] = new_path
					previous_node[neighbor] = current_node

			if current_node == end_node:
				break 
	   
		path = deque()
		current_node = end_node
		while previous_node[current_node] is not None:
			path.appendleft(current_node)
			current_node = previous_node[current_node]
		path.appendleft(start_node)

		return path, distance_from_start[end_node]

def main():
	
	verts,verts_0 = ["B","C","D","E","F","G","H","I"],\
	["B","C","D","E","F"]
	start_0 = time.time()
	for end in  verts:
		verify_algorithm(
			filename="dir.txt",
			start = "A",
			end = end
			)
	end_0 = time.time()
	time_0 = end_0 - start_0
	print(time_0)	
	

	print("*******************")		

	start_1 = time.time()
	for end in  verts_0:
		verify_algorithm(
			filename="ab.txt",
			start = "A",
			end = end
			)
	end_1 = time.time()
	time_1 = end_1 - start_1
	print(time_1)		

	print("*******************")	

	start_2 = time.time()
	for end in  verts:
		verify_algorithm(
			filename="large_graph.txt",
			start = "A",
			end = end
			)

	end_2 = time.time()
	time_2 = end_2 - start_2
	print(time_2)	

def verify_algorithm(filename,start,end):
	
	graph = Graph(filename)
	returned_path, returned_distance = graph.shortest_path(start, end)
	print(" The shortest paths from A to every vertex is {} and their path costs are {}".format(returned_path,returned_distance))
	return
	

if __name__ == "__main__":
	main()