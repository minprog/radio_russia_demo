import random
import copy


def random_assignment(model, possibilities):
    """
    Randomly assign each node with one of the possibilities.
    """
    for node in model.solution:
        model.set_value(node, random.choice(possibilities))


def random_reconfigure_node(model, node, possibilities):
    """
    Takes a node and assigns each node with one of the possibilities.
    """
    model.set_value(node, random.choice(possibilities))


def random_reconfigure_nodes(model, nodes, possibilities):
    """
    Takes a list of nodes and assigns each node with one of the possibilities.
    """
    for node in nodes:
        random_reconfigure_node(model, node, possibilities)


def random_reassignment(model, possibilities):
    """
    Algorithm that reassigns nodes that are invalid until each node is valid.

    CAUTION: may run indefinitely.
    """
    model = model.copy()

    # Randomly assign a value to each of the nodes
    random_assignment(model, possibilities)

    # Find nodes that are "violations" and have neighbours with same value
    violating_nodes = model.get_violations()

    # While we have violations
    while len(violating_nodes):
        # Reconfigure violations randomly
        random_reconfigure_nodes(model, violating_nodes, possibilities)

        # Find nodes that are violations
        violating_nodes = model.get_violations()

    return model
