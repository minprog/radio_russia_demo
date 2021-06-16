import copy
import random

from .randomise import random_reconfigure_node


class HillClimber:
    """
    The HillClimber class that changes a random node in the graph to a random valid value. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, model, transmitters):
        if not model.is_solution():
            raise Exception("HillClimber requires a complete solution.")

        self.model = model
        self.value = model.calculate_value()

        self.transmitters = transmitters

    def mutate_single_node(self, new_model):
        """
        Changes the value of a random node with a random valid value.
        """
        random_node = random.choice(list(new_model.solution))
        available_transmitters = new_model.get_possibilities(random_node, self.transmitters)
        random_reconfigure_node(new_model, random_node, available_transmitters)

    def mutate(self, new_model, number_of_nodes=1):
        """
        Changes the value of a number of nodes with a random valid value.
        """
        for _ in range(number_of_nodes):
            self.mutate_single_node(new_model)

    def check_solution(self, new_model):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = new_model.calculate_value()
        old_value = self.value

        # We are looking for maps that cost less!
        if new_value <= old_value:
            self.model = new_model
            self.value = new_value

    def run(self, iterations, verbose=False, mutate_nodes_number=1):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current value: {self.value}') if verbose else None

            # Create a copy of the model to simulate the change
            new_model = self.model.copy()

            self.mutate(new_model, number_of_nodes=mutate_nodes_number)

            # Accept it if it is better
            self.check_solution(new_model)
