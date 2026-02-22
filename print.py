def create_graph(edges, n):
    graph = {i: [] for i in range(n)}    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u) 
    return graph
edges = [(0, 1), (0, 2), (1, 3), (2, 4)]
n = 5
graph = create_graph(edges, n)
for node in graph:
    print(node, "->", graph[node])