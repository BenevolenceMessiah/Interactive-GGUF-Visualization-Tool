# modules/visualization_tool.py

import json

def get_visualization_data(model):
    """
    Retrieve and prepare data for standard visualizations.

    :param model: Instance of GGUFModel.
    :return: Dictionary containing data for various visualizations.
    """
    if model is None:
        return {}

    # Example: Get attention weights
    attention_weights = [
        [0.1, 0.2, 0.3],
        [0.2, 0.3, 0.4],
        [0.3, 0.4, 0.5]
    ]

    # Example: Get model weights
    weights = [0.5, 0.6, 0.7, 0.8, 0.9]

    # Example: Get node embeddings
    embeddings = [
        [1.0, 2.0, 3.0],
        [2.0, 3.0, 4.0],
        [3.0, 4.0, 5.0]
    ]

    # Prepare data dictionary
    data = {
        "attention": attention_weights,
        "weights": weights,
        "embeddings": embeddings
    }

    return data
