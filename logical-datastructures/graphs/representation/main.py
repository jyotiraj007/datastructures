from graph import Graph
from vertex import Vertex

graph = Graph()

v1 = Vertex('one')
v2 = Vertex('two')
v3 = Vertex('three')
v4 = Vertex('four')
v5 = Vertex('five')
v6 = Vertex('six')

graph.add_vertices(v1)
graph.add_vertices(v2)
graph.add_vertices(v3)
graph.add_vertices(v4)
graph.add_vertices(v5)
graph.add_vertices(v6)

graph.add_edges(v1, v2)
graph.add_edges(v2, v3)
graph.add_edges(v1, v3)
graph.add_edges(v4, v6)
graph.add_edges(v2, v4)
graph.add_edges(v5, v1)
graph.add_edges(v6, v3)

graph.show_graph()

