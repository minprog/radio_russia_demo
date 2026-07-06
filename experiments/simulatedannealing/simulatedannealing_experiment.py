from radio_russia.algorithms import simulatedannealing as sa
from radio_russia.algorithms import randomise
from radio_russia.classes.graph import Graph
from radio_russia.classes.transmitters import CostScheme

import csv
import copy
from statistics import mean


def simulateannealing(graph: Graph, transmitters: CostScheme, scheme: int = 1, iterations: int = 100,
                       output_file: str = "results/simulatedannealing/simulatedannealing.csv") -> None:
    random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(scheme))
    simannealing = sa.SimulatedAnnealing(random_graph, transmitters.get_scheme(scheme))

    print("Running Simulated Annealing...")
    with open(output_file, 'w', newline='') as output_file_handle:
        result_writer = csv.writer(output_file_handle, delimiter=',')

        for _ in range(0, iterations):
            simannealing.run(1)
            result_writer.writerow((simannealing.graph.calculate_value(), simannealing.graph.to_json()))


def simulateannealing_continue(graph: Graph, transmitters: CostScheme, data: str, scheme: int = 1,
                                iterations: int = 100) -> None:
    with open(data, 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        *_, last = result_reader
        json_data = last[1]

    graph.from_json(json_data, transmitters.get_scheme(scheme))
    simannealing = sa.SimulatedAnnealing(graph, transmitters.get_scheme(scheme))

    print("Continueing Simulated Annealing...")
    with open(data, 'a', newline='') as output_file_handle:
        result_writer = csv.writer(output_file_handle, delimiter=',')

        for _ in range(0, iterations):
            simannealing.run(1)
            result_writer.writerow((simannealing.graph.calculate_value(), simannealing.graph.to_json()))

def simulatedannealing_averages(graph: Graph, transmitters: CostScheme, scheme: int = 1, runs: int = 100,
                                 iterations: int = 500,
                                 output_file: str = "results/simulatedannealing/simulatedannealing_averages.csv") -> None:
    results = []
    for i in range(0, runs):
        result = []
        random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(scheme))
        simannealing = sa.SimulatedAnnealing(random_graph, transmitters.get_scheme(scheme))

        print(f"Running Annealing: {i}")

        for _ in range(0, iterations):
                simannealing.run(1)
                result.append(simannealing.graph.calculate_value())

        results.append(result)

    values = []
    for iteration in zip(*results):
        values.append((mean(iteration), min(iteration), max(iteration)))

    with open(output_file, 'w', newline='') as output_file_handle:
        result_writer = csv.writer(output_file_handle, delimiter=',')
        for value in values:
            result_writer.writerow(value)

def simulatedannealing_temperature_comparisons(graph: Graph, transmitters: CostScheme, scheme: int = 1,
                                                runs: int = 100, iterations: int = 500,
                                                temperature_range: tuple[int, int, int] = (1, 60, 10),
                                                output_file_template: str = "results/simulatedannealing/simulatedannealing_temp_{n}.csv") -> None:
    for n in range(*temperature_range):
        results = []
        for i in range(0, runs):
            result = []
            random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(scheme))
            simannealing = sa.SimulatedAnnealing(random_graph, transmitters.get_scheme(scheme), temperature=n)

            print(f"Running Annealing: {i}")

            for _ in range(0, iterations):
                    simannealing.run(1)
                    result.append(simannealing.graph.calculate_value())

            results.append(result)

        values = []
        for iteration in zip(*results):
            values.append((mean(iteration), min(iteration), max(iteration)))

        with open(output_file_template.format(n=n), 'w', newline='') as output_file_handle:
            result_writer = csv.writer(output_file_handle, delimiter=',')
            for value in values:
                result_writer.writerow(value)
