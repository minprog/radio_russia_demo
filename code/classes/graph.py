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
                nodes[int(row['id'])] = Node(row['id'], int(row['id']))

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
                        neighbours.append(int(neighbour.strip('[] ')))

                node_id = int(row['id'])

                # Add the neighbours to the correct node
                for neighbour in neighbours:
                    neighbour = self.nodes[neighbour]
                    self.nodes[node_id].add_neighbour(neighbour)

    def get_nodes(self):
        """
        Returns all nodes in the graph.
        """
        return self.nodes.values()