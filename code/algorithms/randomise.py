import random

from code.classes.model import Model
from code.classes.node import Node

def random_assignment(model: Model) -> None:
    """
    Randomly assign each node with one of the possibilities.
    """
    for node in model.get_nodes():
        model.set_value(node, random.choice(model.get_options()))

def random_reconfigure_node(model: Model, node: Node) -> None:
    """
    Takes a node and assigns each node with one of the possibilities.
    """
    model.set_value(node, random.choice(model.get_possibilities(node)))


def random_reconfigure_nodes(model: Model, nodes: list[Node]) -> None:
    """
    Takes a list of nodes and assigns each node with one of the possibilities.
    """
    for node in nodes:
        random_reconfigure_node(model, node)


def random_reassignment(model: Model) -> Model:
    """
    Algorithm that reassigns nodes that are invalid until each node is valid.

    CAUTION: may run indefinitely.
    """
    new_model = model.copy()

    # Randomly assign a value to each of the nodes
    random_assignment(new_model)

    # Find nodes that are "violations" and have neighbours with same value
    violating_nodes = new_model.get_violations()

    # While we have violations
    while len(violating_nodes):
        # Reconfigure violations randomly
        random_reconfigure_nodes(new_model, violating_nodes)

        # Find nodes that are violations
        violating_nodes = new_model.get_violations()

    return new_model
