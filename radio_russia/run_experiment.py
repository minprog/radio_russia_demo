"""Reproduce a run from its JSON configuration file.

Usage:
    python -m radio_russia.run_experiment experiments/depth_first/depth_first.json
"""
import argparse
import importlib
import json
from pathlib import Path
from types import ModuleType

from radio_russia.classes import graph, transmitters


def load_module(json_path: Path) -> ModuleType:
    folder = json_path.parent.name
    return importlib.import_module(f"experiments.{folder}.{folder}_experiment")


def run_experiment(json_path: Path) -> None:
    with open(json_path, 'r') as config_file:
        config = json.load(config_file)

    data_folder = config["data_folder"]
    scheme = config.get("scheme", 1)

    test_graph = graph.Graph(f"data/{data_folder}/{data_folder}_regions.csv")
    cost_scheme = transmitters.CostScheme("data/transmitters.csv")

    module = load_module(json_path)

    function = getattr(module, config["function"])
    params = config.get("params", {})
    print(f"Running {config['function']}...")
    function(test_graph, cost_scheme, scheme=scheme, **params)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path,
                         help="Path to a run JSON file, e.g. "
                              "experiments/depth_first/depth_first.json")
    args = parser.parse_args()

    run_experiment(args.config)
