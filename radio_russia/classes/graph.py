from __future__ import annotations

import csv
import json

from .node import Node
from .transmitters import Transmitter


class Graph():
    def __init__(self, source_file: str, geo_json: str | None = None) -> None:
        self.nodes = self.load_nodes(source_file)
        self.load_neighbours(source_file)

    def load_nodes(self, source_file: str) -> dict[str, Node]:
        """
        Load all the nodes into the graph.
        """
        nodes = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                nodes[row['id']] = Node(row['id'], row['id'])

        return nodes

    def load_neighbours(self, source_file: str) -> None:
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

    def get_violations(self) -> list[Node]:
        """
        Returns the ids of all nodes that have a neighbour with the same value.
        """
        violations = []

        for node in self.nodes.values():
            if not node.is_valid():
                violations.append(node)

        return violations

    def is_solution(self) -> bool:
        """
        Returns True if each node in the graph is assigned a value.
        False otherwise.
        """
        for node in self.nodes.values():
            if not node.value:
                return False

        return True

    def calculate_value(self) -> int:
        """
        Returns the sum of the values of all nodes.
        """
        value = 0
        for node in self.nodes.values():
            # Allow calculation for partial solutions.
            if node.value:
                value += node.value.value

        return value

    def get_empty_node(self) -> Node | None:
        """
        Returns the first empty node.
        """
        for node in self.nodes.values():
            if not node.value:
                return node

        return None

    def to_json(self) -> str:
        """
        Serialize a graph to a JSON string.
        """
        return json.dumps({node.id: node.value.name for node in self.nodes.values() if node.value is not None})

    def from_json(self, data: str, transmitters: list[Transmitter]) -> None:
        """
        Read and assign node values from a JSON string.
        """
        parsed_data = json.loads(data)

        transmitter_map = {transmitter.name: transmitter for transmitter in transmitters}
        for node, value in parsed_data.items():
            self.nodes[node].value = transmitter_map[value]
