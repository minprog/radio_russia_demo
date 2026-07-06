from radio_russia.algorithms import breadth_first as bf
from radio_russia.classes.graph import Graph
from radio_russia.classes.transmitters import CostScheme
import json


def breadth_first(graph: Graph, transmitters: CostScheme, scheme: int = 1, transmitter_count: int = 4,
                   output_file: str = "results/breadth_first/breadth_first.json") -> None:
    breadth = bf.BreadthFirst(graph, transmitters.get_scheme(scheme)[0:transmitter_count])
    breadth.run()

    with open(output_file, 'w', newline='') as output_file_handle:
        json.dump({
            'visited_state_count': breadth.visited_state_count,
            'max_states_size': breadth.max_states_size,
            'solution_count': breadth.solution_count,
            'states_sizes': breadth.states_sizes,
            'value': breadth.graph.calculate_value(),
            'solution': breadth.graph.to_json()
        }, output_file_handle)


def best_first(graph: Graph, transmitters: CostScheme, scheme: int = 1, transmitter_count: int = 4,
                output_file: str = "results/breadth_first/best_first.json") -> None:
    breadth = bf.BestFirst(graph, transmitters.get_scheme(scheme)[0:transmitter_count])
    breadth.run()

    with open(output_file, 'w', newline='') as output_file_handle:
        json.dump({
            'visited_state_count': breadth.visited_state_count,
            'max_states_size': breadth.max_states_size,
            'solution_count': breadth.solution_count,
            'states_sizes': breadth.states_sizes,
            'value': breadth.graph.calculate_value(),
            'solution': breadth.graph.to_json()
        }, output_file_handle)
