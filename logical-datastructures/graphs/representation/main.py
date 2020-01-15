from graph import Graph
from vertex import Vertex

graph = Graph()

v1 = Vertex('one')
v2 = Vertex('two')
v3 = Vertex('three')
v4 = Vertex('four')
v5 = Vertex('five')
v6 = Vertex('six')

for i in range(ord('A'), ord('E')):
    graph.add_vertices(Vertex(chr(i)))

edges = ['AB', 'AC', 'BD', 'CE', 'BA', 'BE', 'BC', 'CD', 'CA']

for edge in edges:
    graph.add_edges(edge[:1], edge[1:])

graph.show_graph()
