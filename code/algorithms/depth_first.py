import copy


class DepthFirst:
    """
    A Depth First algorithm that builds a stack of graphs with a unique assignment of nodes for each instance.
    """
    def __init__(self, graph, transmitters):
        self.graph = copy.deepcopy(graph)
        self.transmitters = transmitters

        self.states = [copy.deepcopy(self.graph)]

        self.best_solution = None
        self.best_value = float('inf')

        self.visited_state_count = 0
        self.max_states_size = len(self.states)
        self.states_sizes = []
        self.solution_count = 0

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop()

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
            self.states.append(new_graph)

    def check_solution(self, new_graph):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = new_graph.calculate_value()
        old_value = self.best_value

        # We are looking for maps that cost less!
        if new_value <= old_value:
            self.best_solution = new_graph
            self.best_value = new_value

    def size(self):
        return len(self.states)

    def done(self):
        return self.size() == 0
         
    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        while not self.done():
            new_graph = self.get_next_state()

            # Statistical analysis
            self.visited_state_count += 1
            self.max_states_size = max(self.size(), self.max_states_size)
            self.states_sizes.append(self.size())

            # Retrieve the next empty node.
            node = new_graph.get_empty_node()

            if node is not None:
                self.build_children(new_graph, node)
            else:
                self.solution_count += 1
                # Stop if we find a solution
                # self.check_solution(new_graph)
                # break

                # or ontinue looking for better graph
                self.check_solution(new_graph)

        # Update the input graph with the best result found.
        self.graph = self.best_solution

class BranchAndBound(DepthFirst):
    def run(self):
        """
        Runs the algorithm without visiting states worse than encountered.
        """
        while not self.done():
            new_graph = self.get_next_state()

            # Statistical analysis
            self.visited_state_count += 1
            self.max_states_size = max(self.size(), self.max_states_size)
            self.states_sizes.append(self.size())

            # Retrieve the next empty node.
            node = new_graph.get_empty_node()

            if node is not None:
                # Only continue with the branch if it can be better than current best.
                if new_graph.calculate_value() < self.best_value - self.transmitters[0].value:
                    self.build_children(new_graph, node)
            else:
                self.solution_count += 1
                # Stop if we find a solution
                # self.check_solution(new_graph)
                # break

                # or ontinue looking for better graph
                self.check_solution(new_graph)

        # Update the input graph with the best result found.
        self.graph = self.best_solution