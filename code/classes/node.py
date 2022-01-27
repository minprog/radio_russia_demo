class Node():
    def __init__(self, name: str, uid: str):
        self.name = name
        self.id = uid
        self.neighbours = {}
        
    def add_neighbour(self, node: 'Node') -> None:
        """
        Add a neighbour node to the current node.
        """
        self.neighbours[node.id] = node

    def get_neighbours(self) -> list['Node']:
        """
        Returns the neighbouring nodes
        """
        return list(self.neighbours.values())

    def __repr__(self):
        """
        Make sure that the object is printed properly if it is in a list/dict.
        """
        return self.id
