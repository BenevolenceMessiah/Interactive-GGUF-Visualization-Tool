# modules/brain_visualization.py

import json

def prepare_brain_visualization_data(model):
    """
    Prepares data for the 3D brain visualization.

    :param model: Instance of GGUFModel.
    :return: Dictionary containing nodes and links for visualization.
    """
    if model is None:
        return {}

    # Extract nodes and links from the model
    nodes = model.get_brain_nodes()
    links = model.get_brain_links()

    # Prepare the data dictionary
    brain_data = {
        "nodes": nodes,
        "links": links
    }

    return brain_data
