# modules/gguf_model.py

import torch
from llama_cpp import Llama

class GGUFModel:
    def __init__(self, model_path, device, n_ctx=2048, n_gpu_layers=40, n_threads=8):
        """
        Initializes the GGUFModel.

        :param model_path: Path to the GGUF model file.
        :param device: Torch device ('cuda' or 'cpu').
        :param n_ctx: Context length for the model.
        :param n_gpu_layers: Number of layers to offload to GPU.
        :param n_threads: Number of CPU threads for inference.
        """
        self.model_path = model_path
        self.device = device
        self.n_ctx = n_ctx
        self.n_gpu_layers = n_gpu_layers
        self.n_threads = n_threads
        self.model = None

    def load_model(self):
        """
        Loads the GGUF model using the Llama library.
        """
        try:
            self.model = Llama(
                model_path=self.model_path,
                n_ctx=self.n_ctx,
                n_gpu_layers=self.n_gpu_layers,
                n_threads=self.n_threads
            )
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Failed to load model: {e}")
            raise e  # Re-raise the exception after logging

    def unload_model(self):
        """
        Unloads the GGUF model to free up resources.
        """
        if self.model:
            del self.model
            self.model = None
            print("Model unloaded successfully.")

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
        try:
            output = self.model(
                prompt,
                max_tokens=max_tokens,
                stop=stop_tokens
            )
            return output['choices'][0]['text'].strip()
        except Exception as e:
            print(f"Error during inference: {e}")
            return "An error occurred while generating the response."

    def get_brain_nodes(self):
        """
        Extracts nodes (e.g., neurons or layers) from the model for visualization.

        :return: List of dictionaries containing node data.
        """
        nodes = []
        if self.model is None:
            return nodes

        try:
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
        except Exception as e:
            print(f"Error extracting brain nodes: {e}")

        return nodes

    def get_brain_links(self):
        """
        Extracts links (e.g., connections between neurons or layers) from the model for visualization.

        :return: List of dictionaries containing link data.
        """
        links = []
        if self.model is None:
            return links

        try:
            num_layers = self.model.params.n_layers

            for i in range(num_layers - 1):
                link = {
                    "source": f"layer_{i}",
                    "target": f"layer_{i + 1}",
                    "value": self._get_link_weight(i)
                }
                links.append(link)
        except Exception as e:
            print(f"Error extracting brain links: {e}")

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
        try:
            # Replace with actual computation based on model's parameters
            weight = torch.abs(self.model.layers[layer_index].self_attn.norm.weight).mean().item()
            return weight
        except Exception as e:
            print(f"Error computing layer weight for layer {layer_index}: {e}")
            return 0.0

    def _get_link_weight(self, layer_index):
        """
        Computes a weight value for a link between two layers.

        :param layer_index: Index of the source layer.
        :return: Weight value as a float.
        """
        try:
            # Replace with actual computation based on model's parameters
            weight = torch.abs(self.model.layers[layer_index].self_attn.norm.weight).mean().item()
            return weight
        except Exception as e:
            print(f"Error computing link weight for layer {layer_index}: {e}")
            return 0.0
