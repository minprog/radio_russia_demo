import copy
from .node import Node
from .graph import Graph
from .transmitters import Transmitter

class Model:
    def __init__(self, graph:Graph, transmitters:list[Transmitter]):
        self.graph = graph
        self.transmitters = transmitters

        self.solution = {node: None for node in graph.get_nodes()}

    def get_violations(self) -> list[Node]:
        """
        Returns the ids of all nodes that have a neighbour with the same value.
        """
        violations = []

        for node in self.get_nodes():
            if not self.is_valid(node):
                violations.append(node)

        return violations

    def is_solution(self) -> bool:
        """
        Returns True if each node in the graph is assigned a value.
        False otherwise.
        """
        for node in self.get_nodes():
            if not self.has_value(node):
                return False

        return True

    def calculate_value(self) -> int:
        """
        Returns the sum of the values of all nodes.
        """
        total_value = 0

        # Value here is assumed to be a transmitter instance
        for value in self.solution.values():
            # NOTE: Crashes if value is not a Transmitter
            total_value += value.value

        return total_value

    def get_nodes(self) -> list[Node]:
        """
        Return the list of available nodes in the model.
        """
        return list(self.solution.keys())

    def get_options(self) -> list[Transmitter]:
        """
        Return the list of available transmitters in the model.
        """
        return self.transmitters

    def get_empty_node(self) -> Node:
        """
        Returns the first empty node.
        """
        for node in self.get_nodes():
            if not self.has_value(node):
                return node

        return None

    def get_possibilities(self, node:Node) -> list[Transmitter]:
        """
        Returns a list of all available values that can be assigned to this
        node, based on assigned values of neighbours.
        """
        available_options = set(self.get_options())

        unavailable_options = set()
        for neighbour in node.get_neighbours():
            unavailable_options.add(self.solution[neighbour])

        return list(available_options - unavailable_options)

    def is_valid(self, node:Node) -> bool:
        """
        Returns whether the node is valid. A node is valid when there are no
        neighbours with the same value, and it's value is not None.
        """
        if not self.has_value(node):
            return False

        for neighbour in node.get_neighbours():
            if self.solution[neighbour] == self.solution[node]:
                return False

        return True

    def has_value(self, node) -> bool:
        """
        Returns whether the node has an assigned value.
        """
        return self.solution[node] is not None
        
    def set_value(self, node:Node, value:Transmitter) -> None:
        """
        Assigns a value to the node.
        """
        self.solution[node] = value

    def copy(self) -> 'Model':
        """
        Copies a model from itself.
        """
        new_model = copy.copy(self)
        new_model.solution = copy.copy(self.solution)

        return new_model