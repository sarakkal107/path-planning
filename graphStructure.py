from classes.Vertex import Vertex

def add_vertex(vertex, graph):
    v = str([vertex.coords[0],vertex.coords[1]])
    graph[v] = []
    
def add_edge_weight(x1,y1, x2, y2, graph, w):
    #y1, x1 = vertex1[0], vertex1[1]
    #y2, x2 = vertex2[0], vertex2[2]
    v1 = str([x1,y1])
    v2 = str([x2,y2])
    newEdge = [x2,y2,w]
    graph[v1].append([x2,y2])

def print_graph(graph):
    for vertex in graph:
        for adjacent in graph[vertex]:
            print(vertex, "->", adjacent[0], ",", adjacent[1], "  ", adjacent[2])