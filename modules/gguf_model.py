# modules/gguf_model.py

import torch
from llama_cpp import Llama

class GGUFModel:
    def __init__(self, model_path, n_ctx=512, n_gpu_layers=0, n_threads=4):
        self.model_path = model_path
        self.n_ctx = n_ctx
        self.n_gpu_layers = n_gpu_layers
        self.n_threads = n_threads
        self.model = None

    def load_model(self):
        """
        Loads the GGUF model using the Llama library.
        """
        self.model = Llama(
            model_path=self.model_path,
            n_ctx=self.n_ctx,
            n_gpu_layers=self.n_gpu_layers,
            n_threads=self.n_threads
        )

    def unload_model(self):
        """
        Unloads the GGUF model to free up resources.
        """
        if self.model:
            del self.model
            self.model = None

    def generate(self, prompt, max_tokens=50, stop_tokens=None):
        """
        Generates a response from the model based on the input prompt.

        :param prompt: The input text prompt.
        :param max_tokens: The maximum number of tokens to generate.
        :param stop_tokens: Tokens at which generation should stop.
        :return: Generated text response.
        """
        if self.model is None:
            raise ValueError("Model not loaded.")
        output = self.model(
            prompt,
            max_tokens=max_tokens,
            stop=stop_tokens
        )
        return output['choices'][0]['text'].strip()

    def get_brain_nodes(self):
        """
        Extracts nodes (e.g., neurons or layers) from the model for visualization.

        :return: List of dictionaries containing node data.
        """
        nodes = []
        if self.model is None:
            return nodes

        # Example: Extracting layer information as nodes
        num_layers = self.model.params.n_layers
        hidden_size = self.model.params.dim

        for i in range(num_layers):
            node = {
                "id": f"layer_{i}",
                "name": f"Layer {i}",
                "x": i * 15,  # Spatial positioning along the X-axis
                "y": 0,        # Fixed Y-axis for simplicity
                "z": 0,        # Fixed Z-axis for simplicity
                "color": self._get_color(i, num_layers),
                "size": hidden_size / 200,  # Adjust size based on hidden dimensions
                "weight": self._get_layer_weight(i)
            }
            nodes.append(node)
        return nodes

    def get_brain_links(self):
        """
        Extracts links (e.g., connections between neurons or layers) from the model for visualization.

        :return: List of dictionaries containing link data.
        """
        links = []
        if self.model is None:
            return links

        num_layers = self.model.params.n_layers

        for i in range(num_layers - 1):
            link = {
                "source": f"layer_{i}",
                "target": f"layer_{i + 1}",
                "value": self._get_link_weight(i)
            }
            links.append(link)
        return links

    def _get_color(self, index, total):
        """
        Generates a color code based on the node index.

        :param index: The current node index.
        :param total: Total number of nodes.
        :return: Hex color code as a string.
        """
        hue = (index / total) * 360
        return f"hsl({hue}, 70%, 50%)"

    def _get_layer_weight(self, layer_index):
        """
        Computes a weight value for a given layer based on model parameters.

        :param layer_index: Index of the layer.
        :return: Weight value as a float.
        """
        # Placeholder: Replace with actual computation based on model's parameters
        return torch.abs(self.model.layers[layer_index].self_attn.norm.weight).mean().item()

    def _get_link_weight(self, layer_index):
        """
        Computes a weight value for a link between two layers.

        :param layer_index: Index of the source layer.
        :return: Weight value as a float.
        """
        # Placeholder: Replace with actual computation based on model's parameters
        return torch.abs(self.model.layers[layer_index].self_attn.norm.weight).mean().item()
