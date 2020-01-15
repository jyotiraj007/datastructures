from vertex import Vertex


class Graph:
    vertices = {}

    def add_vertices(self, vertex):
        """adds vertices to adjacency list"""
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices.keys():
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edges(self, u, v):
        """ adds edges between two vertices"""
        if u.name in self.vertices and v.name in self.vertices:
            for key, value in self.vertices.items():
                if key == u.name and not any(val.name == v.name for val in value.neighbours):
                    self.vertices[key].add_neighbours(v)
                if key == v.name and not any(val.name == u.name for val in value.neighbours):
                    self.vertices[key].add_neighbours(u)
            return True
        else:
            return False

    def show_graph(self):
        """ Prints the graph """
        for key in self.vertices.keys():
            print(key + '-->' + str(list(self.vertices[key].neighbours)))






