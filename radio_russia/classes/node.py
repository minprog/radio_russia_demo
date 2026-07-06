from __future__ import annotations

from .transmitters import Transmitter


class Node():
    def __init__(self, name: str, uid: str) -> None:
        self.name = name
        self.id = uid
        self.neighbours: dict[str, Node] = {}
        self.value: Transmitter | None = None

    def add_neighbour(self, node: Node) -> None:
        self.neighbours[node.id] = node

    def get_possibilities(self, options: list[Transmitter]) -> list[Transmitter]:
        """
        Returns a list of all available values that can be assigned to this
        node, based on assigned values of neighbours.
        """
        available_options = set(options)

        unavailable_options = set()
        for neighbour in self.neighbours.values():
            unavailable_options.add(neighbour.value)

        return list(available_options - unavailable_options)

    def is_valid(self) -> bool:
        """
        Returns whether the node is valid. A node is valid when there are no
        neighbours with the same value, and it's value is not None.
        """
        if not self.has_value():
            return False

        for neighbour in self.neighbours.values():
            if neighbour.value == self.value:
                return False

        return True

    def has_value(self) -> bool:
        return self.value is not None

    def __repr__(self) -> str:
        """
        Make sure that the object is printed properly if it is in a list/dict.
        """
        return self.id
