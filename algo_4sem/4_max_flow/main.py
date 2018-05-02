import networkx as nx

def ford_fulkerson(graph, source, sink, debug=None):
	flow, path = 0, True
	
	while path:
		# search for path with flow reserve
		path, reserve = depth_first_search(graph, source, sink)
		# print(path)
		# print(reserve)
		flow += reserve
		# increase flow along the path
		for v, u in zip(path, path[1:]):
			if graph.has_edge(v, u):
				graph[v][u]['flow'] += reserve
			else:
				graph[u][v]['flow'] -= reserve
		
		# show intermediate results
		if callable(debug):
			debug(graph, path, reserve, flow)

	# return flow, path

def depth_first_search(graph, source, sink):
	undirected = graph.to_undirected()
	explored = {source}
	stack = [(source, 0, list(undirected[source].items()))]
	
	while stack:
		v, _, neighbours = stack[-1]
		if v == sink:
			break
		
		# search the next neighbour
		while neighbours:
			u, e = neighbours.pop()
			if u not in explored:
				break
		else:
			stack.pop()
			continue
		
		# current flow and capacity
		in_direction = graph.has_edge(v, u)
		capacity = e['capacity']
		flow = e['flow']
		# increase or redirect flow at the edge
		if in_direction and flow < capacity:
			stack.append((u, capacity - flow, list(undirected[u].items())))
			explored.add(u)
		elif not in_direction and flow:
			stack.append((u, flow, list(undirected[u].items())))
			explored.add(u)
	# (source, sink) path and its flow reserve
	reserve = min((f for _, f, _ in stack[1:]), default=0)
	path = [v for v, _, _ in stack]
	
	return path, reserve

if __name__ == '__main__':
	graph = nx.DiGraph()
	graph.add_nodes_from('ABCDEF')
	graph.add_edges_from([
		('A', 'B', {'capacity': 5, 'flow': 3}),
		('A', 'C', {'capacity': 6, 'flow': 3}),
		('A', 'D', {'capacity': 7, 'flow': 4}),
		('B', 'F', {'capacity': 7, 'flow': 3}),
		('C', 'E', {'capacity': 6, 'flow': 3}),
		('C', 'F', {'capacity': 4, 'flow': 3}),
		('D', 'F', {'capacity': 8, 'flow': 4}),
		('E', 'F', {'capacity': 7, 'flow': 3})
	])
	ford_fulkerson(graph, 'A', 'F', print)