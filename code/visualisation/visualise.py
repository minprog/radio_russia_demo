from bokeh.io import show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
import geopandas as gdp
from matplotlib import pyplot as plt


def visualise(graph, geo_file, fast_plot=False):
    """
    Visualisation code that uses bokeh and geometry data from a JSON file
    to represent a coloured graph.
    """
    geo_df = gdp.read_file(geo_file)

    # Get the nodes of the regions in order of uid.
    regions = [node for node in graph.nodes.values()]
    name = [node.id for node in regions]
    cost = [node.get_value().value if node is not None else 0
            for node in regions]
    colour = [node.get_value().colour.get_web() if node is not None else "grey"
              for node in regions]
    transmitter = [node.get_value().name if node is not None else "None"
                   for node in regions]

    geo_df["name"] = name
    geo_df["cost"] = cost
    geo_df["colour"] = colour
    geo_df["transmitter"] = transmitter

    if fast_plot:
        geo_df.plot(color=geo_df["colour"])
        plt.show()
    else:
        # Transform the GeoDataFrame to GeoJSONDataSource.
        geo_source = GeoJSONDataSource(geojson=geo_df.to_json())

        # Set the Bokeh tooltips.
        tooltips = [
            ("(x,y)", "($x, $y)"),
            ("Region", "@name"),
            ("Transmitter", "@transmitter"),
            ("Cost", "@cost")
        ]

        # Make Bokeh plot.
        p = figure(background_fill_color="lightgrey", tooltips=tooltips)
        p.sizing_mode = 'scale_height'
        p.patches(xs='xs', ys='ys', fill_color='colour', line_color='black',
                  line_width=0.2, source=geo_source)
        show(p)
