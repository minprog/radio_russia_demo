from radio_russia.algorithms import greedy as gr
from radio_russia.classes.graph import Graph
from radio_russia.classes.transmitters import CostScheme
import csv


def random_greedy(graph: Graph, transmitters: CostScheme, scheme: int = 1, iterations: int = 10000,
                   output_file: str = "results/greedy/random_greedy.csv") -> None:
    results = []
    for _ in range(iterations):
        random_greedy_graph = gr.RandomGreedy(graph, transmitters.get_scheme(scheme))
        random_greedy_graph.run()
        results.append((random_greedy_graph.graph.calculate_value(), random_greedy_graph.graph.to_json()))

    with open(output_file, 'w', newline='') as output_file_handle:
        result_writer = csv.writer(output_file_handle, delimiter=',')
        for result in results:
            result_writer.writerow(result)


def greedy(graph: Graph, transmitters: CostScheme, scheme: int = 1,
           output_file: str = "results/greedy/greedy.csv") -> None:
    greedy_graph = gr.Greedy(graph, transmitters.get_scheme(scheme))
    greedy_graph.run()
    with open(output_file, 'w', newline='') as output_file_handle:
        result_writer = csv.writer(output_file_handle, delimiter=',')
        result_writer.writerow((greedy_graph.graph.calculate_value(), greedy_graph.graph.to_json()))
