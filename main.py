from code.classes import graph, transmitters

from code.algorithms import randomize

from code.visualisation import visualise as vis

if __name__ == "__main__":
    # Watch out with large datafiles when running depth- and especially
    # breadth-first, since they can be really slow.
    # NOTE: Turn on fast_plot at visualization when selecting Russia!
    data_folder = "usa"

    # Create a graph from our data
    test_graph = graph.Graph(f"data/{data_folder}/{data_folder}_regions.csv")

    # Create the transmitter cost schemes
    transmitters = transmitters.CostScheme("data/transmitters.csv")

    # --------------------------- Random reassignment --------------------------
    random_graph = randomize.random_reassignment(test_graph, transmitters.get_scheme(1))
    print(f"Value of the configuration after Randomized Assignment: "
          f"{random_graph.calculate_value()}")

    # --------------------------- Visualisation --------------------------------
    # Turn fast_plot on for a matplotlib plot, which will be faster than Bokeh.
    # Bokeh will also be too slow for plotting Russia, so turn on when Russia is
    # selected as input!
    fast_plot = False

    vis.visualise(random_graph,
                  f"data/{data_folder}/{data_folder}_regions.shp",
                  fast_plot=fast_plot)
