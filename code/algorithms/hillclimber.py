import copy
import random

from .randomise import random_reconfigure_node

from code.classes.model import Model

class HillClimber:
    """
    The HillClimber class that changes a random node in the model to a random valid value. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, model: Model):
        if not model.is_solution():
            raise Exception("Please provide a complete solution.")

        self.model = model.copy()
        self.value = model.calculate_value()

    def mutate_single_node(self, new_model: Model) -> None:
        """
        Changes the value of a random node with a random valid value.
        """
        random_node = random.choice(new_model.get_nodes())
        random_reconfigure_node(new_model, random_node)

    def mutate_model(self, new_model: Model, number_of_nodes: int=1) -> None:
        """
        Changes the value of a number of nodes with a random valid value.
        """
        for _ in range(number_of_nodes):
            self.mutate_single_node(new_model)

    def check_solution(self, new_model: Model) -> None:
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = new_model.calculate_value()
        old_value = self.value

        # We are looking for maps that cost less!
        if new_value <= old_value:
            self.model = new_model
            self.value = new_value

    def run(self, iterations: int, verbose: bool=False, mutate_nodes_number: int=1) -> None:
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current value: {self.value}') if verbose else None

            # Create a copy of the model to simulate the change
            new_model = self.model.copy()

            self.mutate_model(new_model, number_of_nodes=mutate_nodes_number)

            # Accept it if it is better
            self.check_solution(new_model)
