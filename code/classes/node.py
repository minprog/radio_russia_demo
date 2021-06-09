class Node():
    def __init__(self, name, uid):
        self.name = name
        self.id = uid
        self.neighbours = {}
        self.value = None

    def add_neighbour(self, node):
        self.neighbours[node.id] = node

    def get_possibilities(self, options):
        """
        Returns a list of all available values that can be assigned to this
        node, based on assigned values of neighbours.
        """
        available_options = set(options)

        unavailable_options = set()
        for neighbour in self.neighbours.values():
            unavailable_options.add(neighbour.value)

        return list(available_options - unavailable_options)

    def is_valid(self):
        """
        Returns whether the node is valid. A node is valid when there are no
        neighbours with the same value, and it's value is not None.
        """
        if not self.has_value():
            return False

        for neighbour in self.neighbours.values():
            if neighbour.value == self.value:
                return False

        return True

    def has_value(self):
        return self.value is not None

    def __repr__(self):
        """
        Make sure that the object is printed properly if it is in a list/dict.
        """
        return self.id
