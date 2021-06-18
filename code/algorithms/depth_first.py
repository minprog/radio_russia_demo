import copy
from code.classes.model import Model


class DepthFirst:
    """
    A Depth First algorithm that builds a stack of models with a unique assignment of nodes for each instance.
    """
    def __init__(self, model, transmitters):
        self.model = model.copy()
        self.transmitters = transmitters

        self.states = [model]

        self.best_solution = None
        self.best_value = float('inf')

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop()

    def build_children(self, model, node):
        """
        Creates all possible child-states and adds them to the list of states.
        """
        # Retrieve all valid possible values for the node.
        values = model.get_possibilities(node, self.transmitters)

        # Add an instance of the model to the stack, with each unique value assigned to the node.
        for value in values:
            new_model = model.copy()
            new_model.set_value(node, value)
            self.states.append(new_model)

    def check_solution(self, new_model):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = new_model.calculate_value()
        old_value = self.best_value

        # We are looking for maps that cost less!
        if new_value <= old_value:
            self.best_solution = new_model
            self.best_value = new_value
            print(f"New best value: {self.best_value}")

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        while self.states:
            new_model = self.get_next_state()

            # Retrieve the next empty node.
            node = new_model.get_empty_node()

            if node is not None:
                self.build_children(new_model, node)
            else:
                # Stop if we find a solution
                # self.check_solution(new_model)
                # break

                # or ontinue looking for better solution
                self.check_solution(new_model)

        self.model = self.best_solution