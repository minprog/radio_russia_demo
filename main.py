from code.classes import graph, transmitters
from code.algorithms import randomise
from code.algorithms import greedy as gr
from code.visualisation import visualise as vis

if __name__ == "__main__":
    map_name = "usa"

    # Create a graph from our data
    test_graph = graph.Graph(f"data/{map_name}/{map_name}_regions.csv")

    # Create the transmitter cost schemes
    transmitters = transmitters.CostScheme("data/transmitters.csv")
    scheme = transmitters.get_scheme(1)

    # --------------------------- Random reassignment --------------------------
    random_graph = randomise.random_reassignment(test_graph, scheme)

    print(f"Value of the configuration after Randomised Assignment: "
          f"{random_graph.calculate_value()}")

    # --------------------------- Greedy ---------------------------------------
    greedy = gr.Greedy(test_graph, scheme)
    greedy.run()

    # Note that the result will always be the same!
    print(f"Value of the configuration after Greedy: "
          f"{greedy.graph.calculate_value()}")

    # --------------------------- Random Greedy ---------------------------------
    random_greedy = gr.RandomGreedy(test_graph, scheme)
    random_greedy.run()

    print(f"Value of the configuration after RandomGreedy: "
          f"{random_greedy.graph.calculate_value()}")

    # --------------------------- Visualisation --------------------------------
    vis.visualise(random_greedy.graph,
                  f"data/{map_name}/{map_name}_regions.geojson")
