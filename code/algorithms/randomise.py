import random
import copy


def random_assignment(graph, possibilities):
    """
    Randomly assign each node with one of the possibilities.
    """
    for node in graph.nodes.values():
        node.value = random.choice(possibilities)


def random_reconfigure_node(graph, node, possibilities):
    """
    Takes a node and assigns each node with one of the possibilities.
    """
    node.value = random.choice(possibilities)


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

    # Randomly assign a value to each of the nodes
    random_assignment(new_graph, possibilities)

    # Find nodes that are "violations" and have neighbours with same value
    violating_nodes = new_graph.get_violations()

    # While we have violations
    while len(violating_nodes):
        # Reconfigure violations randomly
        random_reconfigure_nodes(new_graph, violating_nodes, possibilities)

        # Find nodes that are violations
        violating_nodes = new_graph.get_violations()

    return new_graph
