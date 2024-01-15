import csv

from .node import Node


class Graph():
    def __init__(self, source_file, geo_json=None):
        self.nodes = self.load_nodes(source_file)
        self.load_neighbours(source_file)

    def load_nodes(self, source_file):
        """
        Load all the nodes into the graph.
        """
        nodes = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                nodes[row['id']] = Node(row['id'], row['id'])

        return nodes

    def load_neighbours(self, source_file):
        """
        Load all the neighbours into the loaded nodes.
        """
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                neighbours = []

                for neighbour in row['neighbours'].split(','):
                    # Only add if the result is not an empty string
                    if neighbour.strip('[] ') != '':
                        neighbours.append(neighbour.strip('[] '))

                node_id = row['id']

                # Add the neighbours to the correct node
                for neighbour in neighbours:
                    neighbour = self.nodes[neighbour]
                    self.nodes[node_id].add_neighbour(neighbour)

    def calculate_value(self):
        """
        Returns the sum of the values of all nodes.
        """
        result = 0
        for node in self.nodes.values():
            transmitter = node.value
            if not transmitter:
                print("Something is wrong!")
                continue
            result += transmitter.value
        return result



    def is_solution(self):
        """
        Returns True if each node in the graph is assigned a value.
        """
        for node in self.nodes.values():
            if node.value is None:
                return False
        return True

    def is_valid(self):
        """
        Returns True if each node in the graph is assigned a value
        AND none of the nodes have neighbours of the same value.
        """
        for node in self.nodes.values():
            if node.value is None:
                return False
            if not node.is_valid():
                return False
        return True

    def show(self):
        """

        """
        result = ""
        for node in self.nodes.values():
            result += f"Node {node.name} : {node.value} - {', '.join([neighbour.name for neighbour in node.get_neighbours()])}\n"

        if self.is_solution():
            result += f"\n Value: {self.calculate_value()}\n"

        return result