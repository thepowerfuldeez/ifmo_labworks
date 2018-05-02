from collections import defaultdict
from heapq import heappush, heappop
from itertools import count

def minimum_spanning_tree_cost(graph):
	"""PRIM: Return the sum of the costs of the edges in the minimum spanning
	tree for the given graph, which must be a mapping from nodes to an
	iterable of (neighbour, edge-cost) pairs.

	"""
	tiebreak = count().__next__ # Factory for tie-breaking values
	total = 0				   # Total cost of edges in tree
	explored = set()			# Set of vertices in tree
	start = next(iter(graph))   # Arbitrary starting vertex
	unexplored = [(0, tiebreak(), start)] # Unexplored edges ordered by cost
	while unexplored:
		cost, _, winner = heappop(unexplored)
		if winner not in explored:
			explored.add(winner)
			total += cost
			neighbour, cost = graph[winner]
			if neighbour not in explored:
				heappush(unexplored, (cost, tiebreak(), neighbour))
	return total



def make_undirected(cost):
	ucost = {}
	for k, w in cost.items():
		ucost[k] = w
		ucost[(k[1],k[0])] = w
	return ucost

from collections import defaultdict
 
#Class to represent a graph
class Graph:
 
	def __init__(self, graph):
		"""
		:param: graph – adj dict, need to convert to adj matrix
		"""
		self.V = len(graph) #No. of vertices
		self.graph = [[u, v, w] for u, (v, w) in graph.items()] # default dictionary to store graph
		 
  
	# function to add an edge to graph
	def addEdge(self,u,v,w):
		self.graph.append([u,v,w])
 
	# A utility function to find set of an element i
	# (uses path compression technique)
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])
 
	# A function that does union of two sets of x and y
	# (uses union by rank)
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)
 
		# Attach smaller rank tree under root of high rank tree
		# (Union by Rank)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		#If ranks are same, then make one as root and increment
		# its rank by one
		else :
			parent[yroot] = xroot
			rank[xroot] += 1
 
	# The main function to construct MST using Kruskal's algorithm
	def boruvkaMST(self):
		parent = []; rank = []; 
 
		# An array to store index of the cheapest edge of
		# subset. It store [u,v,w] for each component
		cheapest =[]
 
		# Initially there are V different trees.
		# Finally there will be one tree that will be MST
		numTrees = self.V
		MSTweight = 0
 
		# Create V subsets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)
			cheapest =[-1] * self.V
	 
		# Keep combining components (or sets) until all
		# compnentes are not combined into single MST
 
		while numTrees > 1:
 
			# Traverse through all edges and update
			# cheapest of every component
			for i in range(len(self.graph)):
 
				# Find components (or sets) of two corners
				# of current edge
				u, v, w =  self.graph[i]
				try:
					set1 = self.find(parent, u)
				except:
					set1 = 0 
				try:
					set2 = self.find(parent, v)
				except:
					set2 = set1 + 1
 
				# If two corners of current edge belong to
				# same set, ignore current edge. Else check if 
				# current edge is closer to previous
				# cheapest edges of set1 and set2
				if set1 != set2:	
					 
					try:
						if cheapest[set1] == -1 or cheapest[set1][2] > w :
							cheapest[set1] = [u,v,w] 
	 
						if cheapest[set2] == -1 or cheapest[set2][2] > w :
							cheapest[set2] = [u,v,w]
					except: pass
 
			# Consider the above picked cheapest edges and add them
			# to MST
			for node in range(self.V):
 
				#Check if cheapest for current set exists
				if cheapest[node] != -1:
					u,v,w = cheapest[node]
					try:
						set1 = self.find(parent, u)
					except:
						set1 = 0
					try:
						set2 = self.find(parent ,v)
					except:
						set2 = set1 + 1
 
					if set1 != set2 :
						MSTweight += w
						self.union(parent, rank, set1, set2)
						# print ("Edge %d-%d with weight %d included in MST" % (u,v,w))
						numTrees = numTrees - 1
			 
			#reset cheapest array
			cheapest =[-1] * self.V
 
			 
		return MSTweight


import numpy as np
import random
def gen_graph(n, m=10, q=1, r=1e6):
	# m = n * n / 10
	# m = n * n
	g = defaultdict(list)
	for k in range(1, n + 1):
		# g[k] = np.random.choice(n, n // m)
		g[k] = [random.randint(1, n) for _ in range(n // m)]
	
	cost = {}
	for a, b in g.items():
		for c in b:
			cost[(a, c)] = random.randint(q, r)
	return g, cost

import time


def benchmark(n, m=10):
	g, cost = gen_graph(n, m)
	cost = make_undirected(cost)

	g = {k: (a, b) for (k, a), b in cost.items()}

	s, t = 1, 7
	t1 = time.time()
	min_cost = minimum_spanning_tree_cost(g)
	t1 = time.time() - t1
	if n % 1000 == 0:
		print(min_cost)

	t3 = time.time()
	min_cost = Graph(g).boruvkaMST()
	t2 = time.time() - t3
	if n % 1000 == 0:
		print(min_cost)
	return t1, t2

if __name__=='__main__':

	first = []
	second = []
	for n in [100] + list(range(500, 10101, 500)):
		print(n)
		t1_ = []
		t2_ = []
		for _ in range(2):
			t1, t2 = benchmark(n, 10)
			t1_.append(t1)
			t2_.append(t2)
		if t1_ and t2_:
			print(np.mean(t1_), np.mean(t2_))
			first.append(np.mean(t1_))
			second.append(np.mean(t2_))
	for n in [100] + list(range(500, 10101, 500)):
		print(n)
		t1_ = []
		t2_ = []
		for _ in range(2):
			try:
				t1, t2 = benchmark(n, 1)
				t1_.append(t1)
				t2_.append(t2)
			except:
				pass
			print(np.mean(t1_), np.mean(t2_))
			first.append(np.mean(t1_))
			second.append(np.mean(t2_))


	print("A: ")
	print(*first)
	print("B: ")
	print(*second)

	# adj = { 1: [2,3,6],
	#		 2: [1,3,4],
	#		 3: [1,2,4,6],
	#		 4: [2,3,5,7],
	#		 5: [4,6,7],
	#		 6: [1,3,5,7],
	#		 7: [4,5,6]}

	# cost = { (1,2):7,
	#		 (1,3):9,
	#		 (1,6):14,
	#		 (2,3):10,
	#		 (2,4):15,
	#		 (3,4):11,
	#		 (3,6):2,
	#		 (4,5):6,
	#		 (5,6):9,
	#		 (4,7):2,
	#		 (5,7):1,
	#		 (6,7):12}	 