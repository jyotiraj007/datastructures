class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbours(self, vertex):
        self.neighbours.append(vertex)
        # self.neighbours.sort()
