import copy
import random


class Greedy:
    """
    The Greedy class that assigns the best possible value to each node one by one.
    """
    def __init__(self, model, transmitters):
        self.model = model
        self.transmitters = transmitters

    def get_next_node(self, nodes):
        """
        Gets the next node with the most neighbours and removes it from the list.
        """
        nodes.sort(key=lambda node: len(node.neighbours))
        return nodes.pop()

    def run(self):
        """
        Greedily assigns the lowest costing transmitters to the nodes of the graph.
        """
        nodes = list(self.model.solution)

        node_possibilities = self.transmitters

        # Repeat untill no more possible solution or we've assigned all nodes
        while nodes or not node_possibilities:
            node = self.get_next_node(nodes)

            # Retrieve all valid possible values for a node
            node_possibilities = self.model.get_possibilities(node, self.transmitters)

            # Sort them by value in ascending order
            node_possibilities.sort(key=lambda transmitter: transmitter.value)

            # Assign the lowest value possibility to the node
            self.model.set_value(node, node_possibilities[0])


class RandomGreedy(Greedy):
    """
    The Greedy class that assigns the best possible value to each node in random order.
    """
    def get_next_node(self, nodes):
        """
        Gets the next random node and removes it from the list.
        """
        return nodes.pop(random.randrange(0, len(nodes)))
