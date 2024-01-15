from code.classes import graph, transmitters
from code.algorithms.randomise import random_assignment

# from code.visualisation import visualise as vis

if __name__ == "__main__":
    map_name = "nl"

    # Create a graph from our data
    test_graph = graph.Graph(f"data/{map_name}/{map_name}_regions.csv")

    # Create the transmitter cost schemes
    transmitters = transmitters.CostScheme("data/transmitters.csv")
    scheme = transmitters.get_scheme(1)


    # --------------------------- Random assignment --------------------------
    random_assignment(test_graph, scheme)

    print(test_graph.show())

    # --------------------------- Visualisation --------------------------------
    # vis.visualise(climber.graph,
                #   f"data/{data_folder}/{data_folder}_regions.geojson")