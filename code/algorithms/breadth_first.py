from .depth_first import DepthFirst


class BreadthFirst(DepthFirst):
    """"
    A Depth First algorithm that builds a queue of models with a unique assignment of nodes for each instance.

    Almost all of the functions are eqal to those of the DepthFirst class, which is why
    we use that as a parent class.
    """

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.

        For Breadth First we need the first one; we use a queue.
        """
        return self.states.pop(0)
