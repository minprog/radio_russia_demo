class Node():
    def __init__(self, name, uid):
        self.name = name
        self.id = uid
        self.neighbours = {}

    def add_neighbour(self, node):
        self.neighbours[node.id] = node

    def get_neighbours(self):
        """Returns list of own neighbours"""
        return self.neighbours.values()

    def __repr__(self):
        """
        Make sure that the object is printed properly if it is in a list/dict.
        """
        return f"Node({self.name}, {self.id})"

    def __hash__(self):
        return self.id
