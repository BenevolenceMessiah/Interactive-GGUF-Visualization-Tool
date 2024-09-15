# Interactive GGUF Visualization Tool

An interactive tool that visualizes data regarding a GGUF (GPT-Generated Unified Format) file, leveraging Gradio for the web UI, and providing Docker and Jupyter Notebook options for running the program.

## Features

- **Model Overview**: Load and manage GGUF models, adjust parameters, and download models from HuggingFace.
- **Inference**: Interact with the model using a chat interface with Markdown and code support.
- **Visualization**: Visualize layers, attention mechanisms, weights, and node embeddings in 3D.
- **Self-Awareness Experiment**: Explore AI self-awareness through interactive experiments.
- **Unit Tests**: Run unit tests directly from the interface.
- **Audio Integration**: Play audio clips upon certain actions via the batch file.
- **Multiple Execution Options**: Run via Gradio, Docker, or Jupyter Notebook.

## Directory Structure

````Interactive-GGUF-Visualization-Tool/
Interactive-GGUF-Visualization-Tool/
├── audio/
│   ├── Benevolence_Messiah_DJ_Kwe.wav
│   └── New D2.wav
├── models/
│   └── [GGUF models and repositories]
├── modules/
│   ├── data_utils.py
│   ├── download_tool.py
│   ├── gguf_model.py
│   ├── self_awareness_experiment.py
│   ├── visualization_tool.py
│   ├── visualization_utils.py
│   └── brain_visualization.py
├── outputs/
│   └── [Chat session JSON files]
├── tests/
│   └── test_gguf_model.py
├── docs/
│   └── [Documentation files]
├── interactive_gguf_visualization_tool.ipynb
├── gradio_app.py
├── main.py
├── Dockerfile
├── requirements.txt
├── Run_Interactive-GGUF-Visualization-Tool.bat
├── README.md
└── .github/
    └── workflows/
        └── python-app.yml
````


- **`audio/`**: Contains audio files used by the batch script to play sounds.
- **`models/`**: Contains GGUF model files and cloned repositories from HuggingFace.
- **`modules/`**: Contains all Python modules necessary for the application.
- **`outputs/`**: Stores JSON files recording chat sessions.
- **`tests/`**: Contains unit tests for the application.
- **`docs/`**: Contains documentation files.
- **`interactive_gguf_visualization_tool.ipynb`**: Jupyter Notebook for an alternative way to interact with the tool.
- **`gradio_app.py`**: Defines the Gradio web UI.
- **`main.py`**: Entry point for running the Gradio server.
- **`Dockerfile`**: Docker configuration for containerized deployment.
- **`requirements.txt`**: Lists all Python dependencies.
- **`Run_Interactive-GGUF-Visualization-Tool.bat`**: Batch script for Windows to manage installation and execution.
- **`README.md`**: This documentation file.

## Installation

### Prerequisites

- **Python 3.10**
- **Git**
- **Docker Desktop** (optional, for Docker execution)
- **Jupyter Notebook** (optional, for notebook execution)
- **NVIDIA Drivers** supporting CUDA 12.1

### Installation Steps

#### Option 1: Using the Batch Script (Windows Only)

1. **Run the Batch Script**

   Double-click on `Run_Interactive-GGUF-Visualization-Tool.bat` and follow the on-screen prompts to install dependencies, set up the environment, and operate every aspect of the program!

#### Option 2: Manual Installation

1. **Run this series of commands ensuring they all complete succefully**

   ````bash
   git clone https://github.com/BenevolenceMessiah/Interactive-GGUF-Visualization-Tool.git
   cd Interactive-GGUF-Visualization-Tool
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On Unix/Linux
   pip install --upgrade --force-reinstall torch==2.2.0 --index-url https://download.pytorch.org/whl/cu121
   pip install -r requirements.txt
   git clone https://github.com/ggerganov/llama-cpp-python.git
   cd llama-cpp-python
   LLAMA_CUBLAS=1 pip install .
   cd ..
   cd docs
   pip install mkdocs
   mkdocs build
   cd ..
   python main.py  # Gradio
   docker run --gpus all -p 7934:7934 gguf-visualization-tool  # Docker
   jupyter notebook interactive_gguf_visualization_tool.ipynb  # Jupyter Notebook
   ````

## Additional Notes ##
CUDA Support: Ensure that your system has NVIDIA drivers supporting CUDA 12.1 installed. This is crucial for GPU acceleration.
Docker and Gradio Ports: Gradio runs on port 7933 by default, while the Docker container runs on port 7934. They can operate simultaneously without port conflicts.
Batch Script: The Run_Interactive-GGUF-Visualization-Tool.bat script facilitates easy installation and execution on Windows systems. It also manages audio playback and environment setup.

### To Do: ###
- Create Google Colab Notebook to leverage T4 GPU
- Create HuggingFace Space to Leverage whatever free architecture that we can run over there.

---

License
This project is licensed under the MIT License.

Contact
For any inquiries or support, please contact [Benevolence Messiah](https://huggingface.co/BenevolenceMessiah).

---
