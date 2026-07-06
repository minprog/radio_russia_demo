from radio_russia.algorithms import randomise
from radio_russia.classes.graph import Graph
from radio_russia.classes.transmitters import CostScheme
import copy
import csv


def baseline(graph: Graph, transmitters: CostScheme, scheme: int = 1, iterations: int = 10000,
             output_file: str = "results/random/baseline.csv") -> None:
    results = []
    for _ in range(iterations):
        random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(scheme))
        results.append((random_graph.calculate_value(), random_graph.to_json()))

    with open(output_file, 'w', newline='') as output_file_handle:
        result_writer = csv.writer(output_file_handle, delimiter=',')
        for result in results:
            result_writer.writerow(result)
