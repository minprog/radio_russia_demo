class Node():
    def __init__(self, name, uid):
        self.name = name
        self.id = uid
        self.neighbours = set()

    def add_neighbour(self, node):
        """
        Add a node to the collection of neighbours.
        """
        self.neighbours.add(node)

    def get_neighbours(self):
        """
        Returns list of own neighbours
        """
        return list(self.neighbours)

    def __repr__(self):
        """
        Make sure that the object is printed properly if it is in a list/dict.
        """
        return f"Node({self.name}, {self.id})"

    def __hash__(self):
        """
        Makes sure that we can put noeds in set() and as a key in a
        dictionary.
        """
        return self.id
