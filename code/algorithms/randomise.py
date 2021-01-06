import random
import copy


def random_assignment(graph, possibilities):
    """
    Randomly assign each node with one of the possibilities.
    """
    for node in graph.nodes.values():
        node.set_value(random.choice(possibilities))


def random_reconfigure_node(graph, node, possibilities):
    """
    Takes a node and assigns each node with one of the possibilities.
    """
    node.set_value(random.choice(possibilities))


def random_reconfigure_nodes(graph, nodes, possibilities):
    """
    Takes a list of nodes and assigns each node with one of the possibilities.
    """
    for node in nodes:
        random_reconfigure_node(graph, node, possibilities)


def random_reassignment(graph, possibilities):
    """
    Algorithm that reassigns nodes that are invalid until each node is valid.

    CAUTION: may run indefinitely.
    """
    new_graph = copy.deepcopy(graph)

    random_assignment(new_graph, possibilities)

    violating_nodes = new_graph.get_violations()

    while len(violating_nodes):
        random_reconfigure_nodes(new_graph, violating_nodes, possibilities)

        violating_nodes = new_graph.get_violations()

    return new_graph
