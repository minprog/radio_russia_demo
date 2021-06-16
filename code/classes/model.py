class Model():
    def __init__(self, graph):
        self.graph = graph
        self.solution = {node.id: None for node in graph.nodes.values()}

    def get_possibilities(self, node, options):
        """
        Returns a list of all available values that can be assigned to this
        node, based on assigned values of neighbours.
        """
        available_options = set(options)

        unavailable_options = set()
        for neighbour in self.graph.get_neighbours(node):
            unavailable_options.add(self.solution[neighbour.id])

        return list(available_options - unavailable_options)

    def is_valid(self, node):
        """
        Returns whether the node is valid. A node is valid when there are no
        neighbours with the same value, and it's value is not None.
        """
        if not self.has_value(node):
            return False

        for neighbour in self.graph.get_neighbours(node):
            if self.solution[neighbour] == self.solution[node]:
                return False

        return True

    def has_value(self, node):
        """
        Returns a boolean that tells if a node is assigned a value.
        """
        return self.solution[node] is not None

    def get_violations(self):
        """
        Returns all nodes that have a neighbour with the same value.
        """
        violations = []

        for node in self.solution:
            if not self.is_valid(node):
                violations.append(node)

        return violations

    def is_solution(self):
        """
        Returns True if each node in the graph is assigned a value.
        False otherwise.
        """
        for node in self.solution:
            if not self.has_value(node):
                return False

        return True

    def calculate_value(self):
        """
        Returns the sum of the values of all nodes.
        """
        value = 0
        for transmitter in self.solution.values():
            value += transmitter.value

        return value

    def get_empty_node(self):
        """
        Returns the first empty node.
        """
        for node in self.solution:
            if not self.has_value(node):
                return node

        return None

    def set_value(self, node, value):
        """
        Assign a value to a node in the solution.
        """
        self.solution[node] = value

    def get_value(self, node):
        """
        Returns the value corresponding to a node.
        """
        return self.solution[node]

    def copy(self):
        """
        Return a copy of self.
        """
        other = Model(self.graph)
        for node in self.solution:
            other.solution[node] = self.solution[node]
        
        return other