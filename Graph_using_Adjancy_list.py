class GraphUsingAdjancyList:
    def __init__(self):
        self.v=[]
        self.edge={}
    def add_vertex (self,vertex):
        if vertex not in self.v:
            self.v.append(vertex)
            self.edge[vertex]=[]
        else:
            print("vertext already exist")
    def add_edge(self,source,destination,weight=1):
        if source in self.v and destination in self.v:
            #self.edge[source].append(destination,weight)
            #self.edge[source].append((destination, weight))
            self.edge[source].append((destination, weight))
            
        else:
            print("one or both are not found")
    def display(self):
        print("Vertex")
        for vertex in self.v:
            print(f"vertex ----> {vertex}")
        for vertex,neighbour in self.edge.items():
            print(f"{vertex}:{neighbour}")
graph=GraphUsingAdjancyList()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A','B')
graph.add_edge('A','C')
graph.add_edge('A','D')
graph.add_edge('B','C')
graph.add_edge('B','D')
graph.add_edge('C','B')
graph.add_edge('C','D')
graph.display()