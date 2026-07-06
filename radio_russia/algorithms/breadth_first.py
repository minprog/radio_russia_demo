from .depth_first import DepthFirst

from radio_russia.classes.graph import Graph
from radio_russia.classes.node import Node

from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue
import copy

class BreadthFirst(DepthFirst):
    """"
    A Depth First algorithm that builds a queue of graphs with a unique assignment of nodes for each instance.

    Almost all of the functions are eqal to those of the DepthFirst class, which is why
    we use that as a parent class.
    """

    def get_next_state(self) -> Graph:
        """
        Method that gets the next state from the list of states.

        For Breadth First we need the first one; we use a queue.
        """
        return self.states.pop(0)

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)

class BestFirst(BreadthFirst):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(BestFirst, self).__init__(*args, **kwargs)
        self.priority_queue: PriorityQueue[PrioritizedItem] = PriorityQueue()
        self.priority_queue.put(PrioritizedItem(self.graph.calculate_value(), self.graph))

    def build_children(self, graph: Graph, node: Node) -> None:
        """
        Creates all possible child-states and adds them to the list of states.
        """
        # Retrieve all valid possible values for the node.
        values = node.get_possibilities(self.transmitters)

        # Add an instance of the graph to the stack, with each unique value assigned to the node.
        for value in values:
            new_graph = copy.deepcopy(graph)
            new_graph.nodes[node.id].value = value
            self.priority_queue.put(PrioritizedItem(new_graph.calculate_value(), new_graph))

    def size(self) -> int:
        return self.priority_queue.qsize()

    def done(self) -> bool:
        return self.best_solution is not None

    def get_next_state(self) -> Graph:
        """
        Method that gets the next state from the list of states.

        For Best First we need the first one after sorting; we use a queue.

        """
        return self.priority_queue.get().item
