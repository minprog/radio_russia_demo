from bokeh.io import show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
import json

def visualise(model, geo_file):
    """
    Visualisation code that uses bokeh and geometry data from a JSON file
    to represent a coloured graph.
    """
    print("Loading visualisation...")
    with open(geo_file, 'r') as geo_file:
        data = json.load(geo_file)

    # Get the nodes of the regions in order of uid.
    regions = [node for node in model.solution]
    name = [node.id for node in regions]
    cost = [model.get_value(node).value if node is not None else 0
            for node in regions]
    colour = [model.get_value(node).colour.get_web() if node is not None else "grey"
              for node in regions]
    transmitter = [model.get_value(node).name if node is not None else "None"
                   for node in regions]

    for index, region in enumerate(data['features']):
        region['properties']['name'] = name[index]
        region['properties']['cost'] = cost[index]
        region['properties']['colour'] = colour[index]
        region['properties']['transmitter'] = transmitter[index]

    # Transform the GeoDataFrame to GeoJSONDataSource.
    geo_source = GeoJSONDataSource(geojson=json.dumps(data))

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
