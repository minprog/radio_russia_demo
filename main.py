from code.classes import graph, transmitters

from code.algorithms import randomise
from code.algorithms import greedy as gr
from code.algorithms import depth_first as df
from code.algorithms import breadth_first as bf
from code.algorithms import hillclimber as hc
from code.algorithms import simulatedannealing as sa

from code.visualisation import visualise as vis

if __name__ == "__main__":
    # Watch out with large datafiles when running depth- and especially
    # breadth-first, since they can be really slow.
    data_folder = "usa"

    # Create a graph from our data
    test_graph = graph.Graph(f"data/{data_folder}/{data_folder}_regions.csv")

    # Create the transmitter cost schemes
    transmitters = transmitters.CostScheme("data/transmitters.csv")

    # --------------------------- Random reassignment --------------------------
    random_graph = randomise.random_reassignment(test_graph, 
                                                 transmitters.get_scheme(1))
    print(f"Value of the configuration after Randomized Assignment: "
          f"{random_graph.calculate_value()}")

    # --------------------------- Greedy ---------------------------------------
    greedy = gr.Greedy(test_graph, transmitters.get_scheme((1)))
    greedy.run()

    print(f"Value of the configuration after Greedy: "
          f"{greedy.graph.calculate_value()}")

    # --------------------------- Random Greedy ---------------------------------
#     random_greedy = gr.RandomGreedy(test_graph, transmitters.get_scheme((1)))
#     random_greedy.run()

#     print(f"Value of the configuration after RandomGreedy: "
#           f"{random_greedy.graph.calculate_value()}")

    # --------------------------- Depth First ----------------------------------

    # depth = df.DepthFirst(test_graph, transmitters.get_scheme(1)[0:4])
    # depth.run()
    #
    # print(f"Value of the configuration after Depth First: "
    #       f"{depth.graph.calculate_value()}")

    # --------------------------- Breadth First --------------------------------
    # breadth = bf.BreadthFirst(test_graph, transmitters.get_scheme(1)[0:4])
    # breadth.run()
    #
    # print(f"Value of the configuration after Breadth First: "
    #       f"{breadth.graph.calculate_value()}")

    # --------------------------- Hill Climber ---------------------------------
    print("Setting up Hill Climber...")
    climber = hc.HillClimber(random_graph, transmitters.get_scheme(1))

    print("Running Hill Climber...")
    climber.run(2000, verbose=True)

    print(f"Value of the configuration after Hill Climber: "
          f"{climber.graph.calculate_value()}")

    # --------------------------- Simulated Annealing --------------------------
    # It is very difficult to find a good starting temperature for SA. A rule to
    # help you find one is to use the maximum change in score that could happen
    # when mutating your state. In our case, this is 19, because the transmitter
    # maximum difference in score between the most expensive and the cheapest
    # transmitter is 19.

#     print("Setting up Simulated Annealing...")
#     simanneal = sa.SimulatedAnnealing(random_graph, transmitters.get_scheme(1),
#                                       temperature=19)

#     print("Running Simulated Annealing...")
#     simanneal.run(2000, verbose=True)

#     print(f"Value of the configuration after Simulated Annealing: "
#           f"{simanneal.graph.calculate_value()}")

    # --------------------------- Visualisation --------------------------------
    # Turn fast_plot on for a matplotlib plot, which will be faster than Bokeh.
    # Bokeh will also be too slow for plotting Russia, so turn on when Russia is
    # selected as input!
    fast_plot = False

    vis.visualise(climber.graph,
                  f"data/{data_folder}/{data_folder}_regions.geojson")
