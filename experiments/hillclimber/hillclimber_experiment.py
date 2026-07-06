from radio_russia.algorithms import hillclimber as hc
from radio_russia.algorithms import randomise
from radio_russia.classes.graph import Graph
from radio_russia.classes.transmitters import CostScheme

import csv
import copy
from statistics import mean


def hillclimb(graph: Graph, transmitters: CostScheme, scheme: int = 1, iterations: int = 1000,
              output_file: str = "results/hillclimber/hillclimber.csv") -> None:
    random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(scheme))
    climber = hc.HillClimber(random_graph, transmitters.get_scheme(scheme))

    print("Running Hill Climber...")
    with open(output_file, 'w', newline='') as output_file_handle:
        result_writer = csv.writer(output_file_handle, delimiter=',')

        for _ in range(0, iterations):
            climber.run(1)
            result_writer.writerow((climber.graph.calculate_value(), climber.graph.to_json()))


def hillclimb_continue(graph: Graph, transmitters: CostScheme, data: str, scheme: int = 1,
                        iterations: int = 1000) -> None:
    with open(data, 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        *_, last = result_reader
        json_data = last[1]

    graph.from_json(json_data, transmitters.get_scheme(scheme))
    climber = hc.HillClimber(graph, transmitters.get_scheme(scheme))

    print("Continueing Hill Climber...")
    with open(data, 'a', newline='') as output_file_handle:
        result_writer = csv.writer(output_file_handle, delimiter=',')

        for _ in range(0, iterations):
            climber.run(1)
            result_writer.writerow((climber.graph.calculate_value(), climber.graph.to_json()))

def hillclimber_averages(graph: Graph, transmitters: CostScheme, scheme: int = 1, runs: int = 100,
                          iterations: int = 1000,
                          output_file: str = "results/hillclimber/hillclimber_averages.csv") -> None:
    results = []
    for i in range(0, runs):
        result = []
        random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(scheme))
        climber = hc.HillClimber(random_graph, transmitters.get_scheme(scheme))

        print(f"Running Hill Climber: {i}")

        for _ in range(0, iterations):
                climber.run(1)
                result.append(climber.graph.calculate_value())

        results.append(result)

    values = []
    for iteration in zip(*results):
        values.append((mean(iteration), min(iteration), max(iteration)))

    with open(output_file, 'w', newline='') as output_file_handle:
        result_writer = csv.writer(output_file_handle, delimiter=',')
        for value in values:
            result_writer.writerow(value)

def hillclimber_xopt_comparison(graph: Graph, transmitters: CostScheme, scheme: int = 1, runs: int = 100,
                                 iterations: int = 500,
                                 mutate_nodes_range: tuple[int, int] = (1, 6),
                                 output_file_template: str = "results/hillclimber/hillclimber_xopt_{n}.csv") -> None:
    for n in range(*mutate_nodes_range):
        results = []
        for i in range(0, runs):
            result = []
            random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(scheme))
            climber = hc.HillClimber(random_graph, transmitters.get_scheme(scheme))

            print(f"Running Hill Climber: {i}")

            for _ in range(0, iterations):
                climber.run(1, mutate_nodes_number=n)
                result.append(climber.graph.calculate_value())

            results.append(result)

        values = []
        for iteration in zip(*results):
            values.append((mean(iteration), min(iteration), max(iteration)))

        with open(output_file_template.format(n=n), 'w', newline='') as output_file_handle:
            result_writer = csv.writer(output_file_handle, delimiter=',')
            for value in values:
                result_writer.writerow(value)
