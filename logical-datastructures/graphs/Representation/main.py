from graph import Graph
from vertex import Vertex

graph = Graph()

for i in range(ord('A'), ord('E')):
    graph.add_vertices(Vertex(chr(i)))

edges = ['AB', 'AC', 'BD', 'CE', 'BA', 'BE', 'BC', 'CD', 'CA']

for edge in edges:
    graph.add_edges(edge[:1], edge[1:])

graph.show_graph()
