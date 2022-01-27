from code.classes import graph, transmitters
from code.classes import model

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
    data_folder = "nl"

    # Create a graph from our data
    test_graph = graph.Graph(f"data/{data_folder}/{data_folder}_regions.csv")

    # Create the transmitter cost schemes
    transmitters = transmitters.CostScheme("data/transmitters.csv")

    test_model = model.Model(test_graph, transmitters.get_scheme(1))

    # --------------------------- Random reassignment --------------------------
    random_model = randomise.random_reassignment(test_model)
    print(f"Value of the configuration after Randomized Assignment: "
          f"{random_model.calculate_value()}")

    # --------------------------- Greedy ---------------------------------------
    greedy = gr.Greedy(test_model)
    greedy.run()

    print(f"Value of the configuration after Greedy: "
          f"{greedy.model.calculate_value()}")

    # --------------------------- Random Greedy ---------------------------------
    random_greedy = gr.RandomGreedy(test_model)
    random_greedy.run()
    
    print(f"Value of the configuration after RandomGreedy: "
          f"{random_greedy.model.calculate_value()}")

    # --------------------------- Depth First ----------------------------------
    # NOTE: We use [0:4] to only use the first four transmitters to shorten 
    # runtime, but we already know (four colour theorem) that it should be
    # possible...

    depth = df.DepthFirst(test_model)
    depth.model.transmitters = depth.model.transmitters[0:4]
    depth.run()
    
    print(f"Value of the configuration after Depth First: "
          f"{depth.model.calculate_value()}")

    # --------------------------- Breadth First --------------------------------
    # Note: this WILL crash on any of the maps provided, but should work for
    # smaller examples

    breadth = bf.BreadthFirst(test_model)
    breadth.model.transmitters = breadth.model.transmitters[0:4]
    breadth.run(verbose=True)
    
    print(f"Value of the configuration after Breadth First: "
          f"{breadth.model.calculate_value()}")

    # --------------------------- Hill Climber ---------------------------------
    print("Setting up Hill Climber...")
    climber = hc.HillClimber(random_model)

    print("Running Hill Climber...")
    climber.run(2000, verbose=True)

    print(f"Value of the configuration after Hill Climber: "
          f"{climber.model.calculate_value()}")

    # --------------------------- Simulated Annealing --------------------------
    # It is very difficult to find a good starting temperature for SA. A rule to
    # help you find one is to use the maximum change in score that could happen
    # when mutating your state. In our case, this is 19, because the transmitter
    # maximum difference in score between the most expensive and the cheapest
    # transmitter is 19.

    print("Setting up Simulated Annealing...")
    simanneal = sa.SimulatedAnnealing(random_model,
                                      temperature=19)
    
    print("Running Simulated Annealing...")
    simanneal.run(2000, verbose=True)
    
    print(f"Value of the configuration after Simulated Annealing: "
          f"{simanneal.graph.calculate_value()}")

    # --------------------------- Visualisation --------------------------------
    vis.visualise(climber.model,
                  f"data/{data_folder}/{data_folder}_regions.geojson")
