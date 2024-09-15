# modules/download_tool.py

from huggingface_hub import HfApi
import os
import subprocess

def search_models(query):
    """
    Search for models on HuggingFace Hub matching the query.

    :param query: Search query string.
    :return: List of model IDs matching the query.
    """
    api = HfApi()
    results = api.list_models(filter=f"*{query}*")
    model_names = [model.modelId for model in results]
    return model_names

def download_model(model_id, destination_dir='models'):
    """
    Download a model from HuggingFace Hub using Git LFS.

    :param model_id: The ID of the model on HuggingFace Hub.
    :param destination_dir: Directory to save the downloaded model.
    :return: Status message.
    """
    try:
        # Ensure the destination directory exists
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        # Initialize Git LFS
        subprocess.run(["git", "lfs", "install"], check=True)
        # Clone the repository into the destination directory
        repo_name = model_id.split('/')[-1]
        clone_path = os.path.join(destination_dir, repo_name)
        subprocess.run(["git", "clone", f"https://huggingface.co/{model_id}", clone_path], check=True)
        return f"Model '{repo_name}' downloaded successfully."
    except subprocess.CalledProcessError as e:
        return f"Error downloading model: {e}"
