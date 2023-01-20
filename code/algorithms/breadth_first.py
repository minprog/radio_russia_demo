from .depth_first import DepthFirst

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

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.

        For Breadth First we need the first one; we use a queue.
        """
        return self.states.pop(0)

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

class BestFirst(BreadthFirst):
    def __init__(self, *args, **kwargs):
        super(BestFirst, self).__init__(*args, **kwargs)
        self.states = PriorityQueue()
        self.states.put(PrioritizedItem(self.graph.calculate_value(), self.graph))

    def build_children(self, graph, node):
        """
        Creates all possible child-states and adds them to the list of states.
        """
        # Retrieve all valid possible values for the node.
        values = node.get_possibilities(self.transmitters)

        # Add an instance of the graph to the stack, with each unique value assigned to the node.
        for value in values:
            new_graph = copy.deepcopy(graph)
            new_graph.nodes[node.id].value = value
            self.states.put(PrioritizedItem(new_graph.calculate_value(), new_graph))
    
    def size(self):
        return self.states.qsize()

    def done(self):
        return self.best_solution

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.

        For Best First we need the first one after sorting; we use a queue.

        """
        return self.states.get().item
