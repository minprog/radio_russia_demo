import csv
from colour import Color
from collections import defaultdict


class CostScheme:
    def __init__(self, transmitter_file: str):
        self.schemes = self.load_transmitters(transmitter_file)

    def load_transmitters(self, transmitter_file: str) -> dict[int, list['Transmitter']]:
        """
        Load all the transmitters into the table.
        """
        schemes = defaultdict(list)
        with open(transmitter_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            # Unpack the reader to determine length for colour range
            rows = list(reader)
            red = Color("red")
            colours = list(red.range_to(Color("blue"), len(rows)))

            # Add a transmitter for each of it's schemes
            for count, row in enumerate(rows):
                costs = eval(row['costs'])
                for index, cost in enumerate(costs):
                    schemes[index].append(Transmitter(row['transmitter'], cost, colours[count]))

        return schemes

    def get_scheme(self, index: int) -> list['Transmitter']:
        """
        Returns the transmitters of a specific cost scheme.
        """
        if index in self.schemes:
            return self.schemes[index]

        raise KeyError("Scheme does not exist.")


class Transmitter:
    """
    Dataclass containing transmitter info.
    """
    def __init__(self, name: str, value: int, colour: Color):
        self.name = name
        self.value = value
        self.colour = colour

    def __hash__(self):
        """
        Makes sure that we can put transmitters in set() and as a key in a
        dictionary.
        """
        return hash(self.name)

    def __eq__(self, other: 'Transmitter'):
        """
        Makes sure that we can compare different transmitters by checking
        whether two elements are both Transmitter, and whether they have the
        same name.
        """
        return self.__class__ == other.__class__ and self.name == other.name
