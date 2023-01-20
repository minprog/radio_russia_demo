from code.classes import graph, transmitters

from code.algorithms import randomise
from code.algorithms import greedy as gr
from code.algorithms import depth_first as df
from code.algorithms import breadth_first as bf
from code.algorithms import hillclimber as hc
from code.algorithms import simulatedannealing as sa

from experiments.random import random_experiment
from experiments.greedy import greedy_experiment
from experiments.depth_first import depth_first_experiment
from experiments.breadth_first import breadth_first_experiment
from experiments.hillclimber import hillclimber_experiment
from experiments.simulatedannealing import simulatedannealing_experiment

from code.visualisation import visualise as vis

if __name__ == "__main__":
    # Watch out with large datafiles when running depth- and especially
    # breadth-first, since they can be really slow.
    data_folder = "nl"

    # Create a graph from our data
    test_graph = graph.Graph(f"data/{data_folder}/{data_folder}_regions.csv")

    # Create the transmitter cost schemes
    transmitters = transmitters.CostScheme("data/transmitters.csv")

    # --------------------------- Random reassignment --------------------------
    # random_graph = randomise.random_reassignment(test_graph,
    #                                              transmitters.get_scheme(1))
    # print(f"Value of the configuration after Randomized Assignment: "
    #       f"{random_graph.calculate_value()}")

    # random_experiment.baseline(test_graph, transmitters)
    # random_experiment.baseline_graph()


    # --------------------------- Greedy ---------------------------------------
    # greedy = gr.Greedy(test_graph, transmitters.get_scheme((1)))
    # greedy.run()

    # print(f"Value of the configuration after Greedy: "
    #       f"{greedy.graph.calculate_value()}")

    # --------------------------- Random Greedy ---------------------------------
    # random_greedy = gr.RandomGreedy(test_graph, transmitters.get_scheme((1)))
    # random_greedy.run()
    #
    # print(f"Value of the configuration after RandomGreedy: "
    #       f"{random_greedy.graph.calculate_value()}")

    # greedy_experiment.random_greedy(test_graph, transmitters)
    # greedy_experiment.greedy(test_graph, transmitters)
    # greedy_experiment.random_greedy_graph()
    # greedy_experiment.base_vs_random_graph()

    # --------------------------- Depth First ----------------------------------
    # NOTE: We use [0:4] to only use the first four transmitters, which makes this
    # take longer, but we already know (four colour theorem) that it should be
    # possible...

    # depth = df.DepthFirst(test_graph, transmitters.get_scheme(1)[0:4])
    # depth.run()
    
    # print(f"Value of the configuration after Depth First: "
    #       f"{depth.graph.calculate_value()}")

    # depth_first_experiment.depth_first(test_graph, transmitters)
    # depth_first_experiment.branchandbound(test_graph, transmitters)
    # depth_first_experiment.depth_first_table()
    # depth_first_experiment.depth_first_memory_graph()
    # depth_first_experiment.depth_first_memory_comparison()

    # --------------------------- Breadth First --------------------------------
    # Note: this WILL crash on any of the maps provided, but should work for
    # smaller examples

    # breadth = bf.BreadthFirst(test_graph, transmitters.get_scheme(1)[0:4])
    # breadth.run()
    #
    # print(f"Value of the configuration after Breadth First: "
    #       f"{breadth.graph.calculate_value()}")

    # breadth_first_experiment.breadth_first(test_graph, transmitters)
    # breadth_first_experiment.best_first(test_graph, transmitters)
    # breadth_first_experiment.breadth_first_table()
    # breadth_first_experiment.breadth_first_memory_graph()
    # breadth_first_experiment.breadth_first_memory_comparison()
    # breadth_first_experiment.constructive_memory_comparison()
    # breadth_first_experiment.constructive_comparison()

    # --------------------------- Hill Climber ---------------------------------
    # print("Setting up Hill Climber...")
    # climber = hc.HillClimber(random_graph, transmitters.get_scheme(1))

    # print("Running Hill Climber...")
    # climber.run(2000, verbose=True)

    # print(f"Value of the configuration after Hill Climber: "
    #       f"{climber.graph.calculate_value()}")

    # hillclimber_experiment.hillclimb(test_graph, transmitters)
    # hillclimber_experiment.hillclimb_continue(test_graph, transmitters, "results/hillclimber/hillclimber.csv")
    # hillclimber_experiment.hillclimb_graph()

    # hillclimber_experiment.hillclimber_averages(test_graph, transmitters)
    # hillclimber_experiment.hillclimber_averages_graph()
    # hillclimber_experiment.hillclimber_averages_filled_graph()

    # hillclimber_experiment.hillclimber_xopt_comparison(test_graph, transmitters)
    # hillclimber_experiment.hillclimber_xopt_comparison_graph()

    # --------------------------- Simulated Annealing --------------------------
    # It is very difficult to find a good starting temperature for SA. A rule to
    # help you find one is to use the maximum change in score that could happen
    # when mutating your state. In our case, this is 19, because the transmitter
    # maximum difference in score between the most expensive and the cheapest
    # transmitter is 19.

    # print("Setting up Simulated Annealing...")
    # simanneal = sa.SimulatedAnnealing(random_graph, transmitters.get_scheme(1),
    #                                   temperature=19)
    #
    # print("Running Simulated Annealing...")
    # simanneal.run(2000, verbose=True)
    #
    # print(f"Value of the configuration after Simulated Annealing: "
    #       f"{simanneal.graph.calculate_value()}")

    # --------------------------- Visualisation --------------------------------
    # vis.visualise(climber.graph,
    #               f"data/{data_folder}/{data_folder}_regions.geojson")

    # simulatedannealing_experiment.simulateannealing(test_graph, transmitters)
    # simulatedannealing_experiment.simulateannealing_continue(test_graph, transmitters, "results/simulatedannealing/simulatedannealing.csv")
    # simulatedannealing_experiment.simulateannealing_graph()

    # simulatedannealing_experiment.simulatedannealing_averages(test_graph, transmitters)
    # simulatedannealing_experiment.simulatedannealing_averages_graph()
    # simulatedannealing_experiment.simulatedannealing_averages_filled_graph()

    # simulatedannealing_experiment.simulatedannealing_temperature_comparisons(test_graph, transmitters)
    simulatedannealing_experiment.simulatedannealing_temperature_comparisons_graph()
