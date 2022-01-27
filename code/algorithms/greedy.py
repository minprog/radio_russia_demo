import random
from code.classes.model import Model
from code.classes.node import Node

class Greedy:
    """
    The Greedy class that assigns the best possible value to each node one by one.
    """
    def __init__(self, model: Model):
        self.model = model.copy()

    def get_next_node(self, nodes: list[Node]) -> Node:
        """
        Gets the next node with the most neighbours and removes it from the list.
        """
        nodes.sort(key=lambda node: len(node.get_neighbours()))
        return nodes.pop()

    def run(self) -> None:
        """
        Greedily assigns the lowest costing transmitters to the nodes of the model.
        """
        nodes = list(self.model.get_nodes())

        node_possibilities = self.model.get_options()

        # Repeat untill no more possible solution or we've assigned all nodes
        while not self.model.is_solution():
            node = self.get_next_node(nodes)

            # Retrieve all valid possible values for a node
            node_possibilities = self.model.get_possibilities(node)

            if not node_possibilities:
                break

            # Sort them by value in ascending order
            node_possibilities.sort(key=lambda transmitter: transmitter.value)

            # Assign the lowest value possibility to the node
            self.model.set_value(node, node_possibilities[0])


class RandomGreedy(Greedy):
    """
    The Greedy class that assigns the best possible value to each node in random order.
    """
    def get_next_node(self, nodes: list[Node]) -> Node:
        """
        Gets the next random node and removes it from the list.
        """
        return nodes.pop(random.randrange(0, len(nodes)))
