class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbours(self, neighbour_vertex):
        if neighbour_vertex not in self.neighbours:
            self.neighbours.append(neighbour_vertex)
            self.neighbours.sort()
