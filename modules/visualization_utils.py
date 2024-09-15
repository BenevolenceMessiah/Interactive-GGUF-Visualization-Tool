# visualization_utils.py

import numpy as np
import json

def prepare_layer_visualization_data(input_text, output_text):
    """
    Prepare data for visualizing input and output text in 3D.

    :param input_text: Input text string.
    :param output_text: Generated output text string.
    :return: JSON data suitable for 3D visualization.
    """
    # Example: Convert text to ASCII codes for visualization
    input_codes = [ord(c) for c in input_text]
    output_codes = [ord(c) for c in output_text]

    # Generate 3D coordinates (placeholder example)
    input_coords = [{"x": i, "y": code, "z": 0} for i, code in enumerate(input_codes)]
    output_coords = [{"x": i, "y": code, "z": 1} for i, code in enumerate(output_codes)]

    data = {
        "input": input_coords,
        "output": output_coords
    }
    return json.dumps(data)

def prepare_attention_data(attention_weights):
    """
    Prepare attention weights for visualization.

    :param attention_weights: Attention weights from the model.
    :return: JSON data suitable for heatmap or graph visualization.
    """
    data = attention_weights.tolist()
    return json.dumps(data)

def prepare_weight_data(weights):
    """
    Prepare model weights for visualization.

    :param weights: Model weights.
    :return: JSON data suitable for 3D visualization.
    """
    flattened_weights = weights.flatten()
    coords = [{"x": i, "y": w, "z": 0} for i, w in enumerate(flattened_weights)]
    return json.dumps(coords)

def prepare_embedding_data(embeddings):
    """
    Prepare node embeddings for visualization.

    :param embeddings: Node embeddings from the model.
    :return: JSON data suitable for 3D visualization.
    """
    coords = [{"x": emb[0], "y": emb[1], "z": emb[2]} for emb in embeddings]
    return json.dumps(coords)
