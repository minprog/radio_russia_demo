class Node():
    def __init__(self, name, uid):
        self.name = name
        self.id = uid

        self._neighbours = []
        self.value = None

    def add_neighbour(self, node):
        self._neighbours.append(node)

    def get_neighbours(self):
        return self._neighbours

    def is_valid(self):
        """
        Returns whether the node is valid. A node is valid when there are
        no neighbours with the same value.
        """
        # If the value is not None
        if not self.value:
            return False

        for neighbour in self.get_neighbours():
            if neighbour.value is self.value:
                return False

        return True