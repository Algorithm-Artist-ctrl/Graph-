class GraphusingEdgeList:
    
    def __init__(self):
        self.v=[]
        self.edge=[]
    def add_vertex (self,vertex):
        if vertex not in self.v:
            self.v.append(vertex)
        else:
            print(f"{vertex} already exist")
    def add_edge (self,source,destination):
        if source in self.v and destination in self.v :
            edge=(source,destination)
            self.edge.append(edge)
        else:
            print("one or both vertices are not found ")
    
    def display (self):
        print("Vertices")
        for vertex in self.v:
            print(f"{vertex}")
        
        for source,destination in self.edge:
            print(f"{source} -----> {destination}")

graph=GraphusingEdgeList()
graph.add_vertex(20)
graph.add_vertex(21)
graph.add_vertex(22)
graph.add_vertex(19)
graph.add_vertex(23)
graph.add_edge(19,20)
graph.add_edge(20,21)
graph.add_edge(21,22)
graph.add_edge(22,23)
graph.display()