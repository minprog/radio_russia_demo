import random
import math

from .hillclimber import HillClimber


class SimulatedAnnealing(HillClimber):
    """
    The SimulatedAnnealing class that changes a random node in the graph to a random valid value.
    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.

    Most of the functions are similar to those of the HillClimber class, which is why
    we use that as a parent class.
    """
    def __init__(self, model, transmitters, temperature=1):
        # Use the init of the Hillclimber class
        super().__init__(model, transmitters)

        # Starting temperature and current temperature
        self.T0 = temperature
        self.T = temperature

    def update_temperature(self):
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        self.T = self.T - (self.T0 / self.iterations)

        # Exponential would look like this:
        # alpha = 0.99
        # self.T = self.T * alpha

        # where alpha can be any value below 1 but above 0

    def check_solution(self, model):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        new_value = model.calculate_value()
        old_value = self.value

        # Calculate the probability of accepting this new graph
        delta = new_value - old_value
        probability = math.exp(-delta / self.T)

        # NOTE: Keep in mind that if we want to maximize the value, we use:
        # delta = old_value - new_value

        # Pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.model = model
            self.value = new_value

        # Update the temperature
        self.update_temperature()
