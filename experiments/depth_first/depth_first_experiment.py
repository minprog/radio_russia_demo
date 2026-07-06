from radio_russia.algorithms import depth_first as df
from radio_russia.classes.graph import Graph
from radio_russia.classes.transmitters import CostScheme
import json

def depth_first(graph: Graph, transmitters: CostScheme, scheme: int = 1, transmitter_count: int = 4,
                 output_file: str = "results/depth_first/depth_first.json") -> None:
    depth = df.DepthFirst(graph, transmitters.get_scheme(scheme)[0:transmitter_count])
    depth.run()

    with open(output_file, 'w', newline='') as output_file_handle:
        json.dump({
            'visited_state_count': depth.visited_state_count,
            'max_states_size': depth.max_states_size,
            'solution_count': depth.solution_count,
            'states_sizes': depth.states_sizes,
            'value': depth.graph.calculate_value(),
            'solution': depth.graph.to_json()
        }, output_file_handle)

def branchandbound(graph: Graph, transmitters: CostScheme, scheme: int = 1, transmitter_count: int = 4,
                    output_file: str = "results/depth_first/branchandbound.json") -> None:
    depth = df.BranchAndBound(graph, transmitters.get_scheme(scheme)[0:transmitter_count])
    depth.run()

    with open(output_file, 'w', newline='') as output_file_handle:
        json.dump({
            'visited_state_count': depth.visited_state_count,
            'max_states_size': depth.max_states_size,
            'solution_count': depth.solution_count,
            'states_sizes': depth.states_sizes,
            'value': depth.graph.calculate_value(),
            'solution': depth.graph.to_json()
        }, output_file_handle)
