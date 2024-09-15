# data_utils.py

import os
import json
from datetime import datetime

def ensure_directory_exists(directory):
    """
    Ensure that the specified directory exists.

    :param directory: Directory path.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_chat(prompt, response):
    """
    Save the chat session to a JSON file.

    :param prompt: User input.
    :param response: Model's response.
    """
    ensure_directory_exists('outputs')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    chat_file = os.path.join('outputs', f"chat_{timestamp}.json")
    chat_data = {
        "prompt": prompt,
        "response": response
    }
    with open(chat_file, 'w') as f:
        json.dump(chat_data, f)

def load_chat(chat_file):
    """
    Load a chat session from a JSON file.

    :param chat_file: Chat file name.
    :return: Chat data.
    """
    chat_path = os.path.join('outputs', chat_file)
    with open(chat_path, 'r') as f:
        chat_data = json.load(f)
    return chat_data
