class Node():
    def __init__(self, name, uid):
        self.name = name
        self.id = uid
        self.neighbours = {}

    def add_neighbour(self, node):
        self.neighbours[node.id] = node

    def __repr__(self):
        """
        Make sure that the object is printed properly if it is in a list/dict.
        """
        return self.id

    def __hash__(self):
        return self.id
