import argparse
from pathlib import Path

from radio_russia.classes.graph import Graph
from radio_russia.classes.transmitters import CostScheme, Transmitter
from radio_russia.algorithms import randomise
from radio_russia.algorithms import greedy as gr
from radio_russia.algorithms import depth_first as df
from radio_russia.algorithms import breadth_first as bf
from radio_russia.algorithms import hillclimber as hc
from radio_russia.algorithms import simulatedannealing as sa
from radio_russia.visualisation import visualise as vis
from radio_russia.run_experiment import run_experiment

ALGORITHMS = [
    "random", "greedy", "random-greedy", "depth-first", "branch-and-bound",
    "breadth-first", "best-first", "hillclimber", "simulated-annealing",
]


def build_graph_and_transmitters(data_folder: str, scheme: int) -> tuple[Graph, list[Transmitter]]:
    test_graph = Graph(f"data/{data_folder}/{data_folder}_regions.csv")
    cost_scheme = CostScheme("data/transmitters.csv")
    return test_graph, cost_scheme.get_scheme(scheme)


def run_algorithm(args: argparse.Namespace) -> None:
    test_graph, transmitters = build_graph_and_transmitters(args.data_folder, args.scheme)

    if args.algorithm == "random":
        result_graph = randomise.random_reassignment(test_graph, transmitters)
    elif args.algorithm == "greedy":
        greedy = gr.Greedy(test_graph, transmitters)
        greedy.run()
        result_graph = greedy.graph
    elif args.algorithm == "random-greedy":
        random_greedy = gr.RandomGreedy(test_graph, transmitters)
        random_greedy.run()
        result_graph = random_greedy.graph
    elif args.algorithm == "depth-first":
        # NOTE: full transmitter sets can take very long, hence --transmitter-count.
        depth = df.DepthFirst(test_graph, transmitters[0:args.transmitter_count])
        depth.run()
        result_graph = depth.graph
    elif args.algorithm == "branch-and-bound":
        depth = df.BranchAndBound(test_graph, transmitters[0:args.transmitter_count])
        depth.run()
        result_graph = depth.graph
    elif args.algorithm == "breadth-first":
        # NOTE: this WILL crash on any of the maps provided, but should work
        # for smaller examples.
        breadth = bf.BreadthFirst(test_graph, transmitters[0:args.transmitter_count])
        breadth.run()
        result_graph = breadth.graph
    elif args.algorithm == "best-first":
        breadth = bf.BestFirst(test_graph, transmitters[0:args.transmitter_count])
        breadth.run()
        result_graph = breadth.graph
    elif args.algorithm == "hillclimber":
        random_graph = randomise.random_reassignment(test_graph, transmitters)
        climber = hc.HillClimber(random_graph, transmitters)
        climber.run(args.iterations, verbose=True)
        result_graph = climber.graph
    elif args.algorithm == "simulated-annealing":
        # A good starting temperature is the maximum change in score that
        # could happen when mutating a state.
        random_graph = randomise.random_reassignment(test_graph, transmitters)
        simanneal = sa.SimulatedAnnealing(random_graph, transmitters, temperature=args.temperature)
        simanneal.run(args.iterations, verbose=True)
        result_graph = simanneal.graph
    else:
        raise ValueError(f"Unknown algorithm: {args.algorithm}")

    print(f"Value of the configuration after {args.algorithm}: {result_graph.calculate_value()}")

    if args.visualise:
        vis.visualise(result_graph, f"data/{args.data_folder}/{args.data_folder}_regions.geojson")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m radio_russia",
                                      description="Place transmitters to broadcast radio signal into Russia.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    algorithm_parser = subparsers.add_parser("algorithm", help="Run a single algorithm on a dataset.")
    algorithm_parser.add_argument("algorithm", choices=ALGORITHMS, help="The algorithm to run.")
    algorithm_parser.add_argument("--data-folder", default="nl",
                                   help="Name of the data folder under data/, e.g. nl, usa, china.")
    algorithm_parser.add_argument("--scheme", type=int, default=1, help="Cost scheme index to use.")
    algorithm_parser.add_argument("--transmitter-count", type=int, default=4,
                                   help="Number of transmitter types to use "
                                        "(depth-first/branch-and-bound/breadth-first/best-first only).")
    algorithm_parser.add_argument("--iterations", type=int, default=2000,
                                   help="Number of iterations (hillclimber/simulated-annealing only).")
    algorithm_parser.add_argument("--temperature", type=float, default=19,
                                   help="Starting temperature (simulated-annealing only).")
    algorithm_parser.add_argument("--visualise", action="store_true",
                                   help="Show a bokeh visualisation of the resulting configuration.")

    experiment_parser = subparsers.add_parser("experiment", help="Run an experiment from its JSON configuration "
                                                                  "and plot its results.")
    experiment_parser.add_argument("config", type=Path,
                                    help="Path to an experiment JSON file, e.g. "
                                         "experiments/depth_first/depth_first_experiment.json")

    return parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "algorithm":
        run_algorithm(args)
    elif args.command == "experiment":
        run_experiment(args.config)
    else:
        raise ValueError(f"Unknown command: {args.command}")
