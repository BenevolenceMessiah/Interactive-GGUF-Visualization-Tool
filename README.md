# 🌟 Interactive GGUF Visualization Tool 🌟

As-salamu alaikum; welcome to the **Interactive GGUF Visualization Tool** —your ultimate companion for exploring, interacting with, and visualizing GPT-Generated Unified Format (GGUF) models. Whether you're a researcher, developer, or AI enthusiast, this tool offers a seamless and immersive experience to delve deep into the intricacies of GGUF models.

## 🔍 What is GGUF?

GGUF (GPT-Generated Unified Format) is a standardized format designed to encapsulate the complexities of GPT models, enabling streamlined interactions, enhanced performance, and versatile integrations across various platforms and applications.

## 🚀 Key Features

### 🌐 **Model Overview**
- **Load & Manage Models:** Effortlessly load GGUF models from your local repository or download them directly from [HuggingFace](https://huggingface.co/).
- **Parameter Tuning:** Adjust crucial parameters such as context length, GPU layers, and CPU threads to optimize performance.
- **Repository Integration:** Seamlessly clone and manage GGUF repositories, ensuring you always work with the latest model iterations.

### 💬 **Inference Interface**
- **Interactive Chatbot:** Engage with your GGUF models through a dynamic chat interface that supports Markdown and code snippets.
- **Real-time Responses:** Experience swift and accurate responses powered by your loaded GGUF models.
- **Chat History:** Save and revisit your chat sessions, allowing for continuous and context-aware interactions.

### 🎨 **Advanced Visualization**
- **3D Brain Visualization:** Dive into a stunning 3D representation of your GGUF model's architecture, showcasing layers, connections, and weights.
- **Layer & Attention Heatmaps:** Visualize attention mechanisms and layer-wise activations to gain deeper insights into model behaviors.
- **Weight & Embedding Charts:** Analyze model weights and node embeddings through interactive bar charts and scatter plots.

### 🧠 **Self-Awareness Experiment**
- **AI Self-Reflection:** Conduct experiments to explore AI self-awareness, posing self-referential questions and analyzing responses.
- **Interactive Exploration:** Customize prompts and observe how your GGUF models interpret and respond to complex queries.

### 🧪 **Comprehensive Testing**
- **Unit Tests:** Ensure the robustness and reliability of your application with integrated unit tests.
- **Notebook Execution:** Validate Jupyter Notebooks directly through the interface, maintaining code integrity and performance.

### 🎵 **Audio Integration**
- **Engaging Feedback:** Enjoy audio clips that play during specific actions, enhancing the interactive experience via the batch script.

### ⚙️ **Flexible Execution Options**
- **Gradio Web UI:** Access a user-friendly web interface for all functionalities.
- **Docker Containerization:** Deploy and run the tool in isolated environments using Docker for consistent performance.
- **Jupyter Notebook Compatibility:** Interact with the tool through Jupyter Notebooks

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
│   └── [Documentation files, optional]
├── interactive_gguf_visualization_tool.ipynb
├── gradio_app.py
├── main.py
├── Dockerfile
├── requirements.txt
├── Run_Interactive-GGUF-Visualization-Tool.bat
├── README.md
├── .gitignore
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
- **`.gitignore:`**: Specifies files and directories to be ignored by Git.
- **`.github/workflows/python-app.yml`**: GitHub Actions workflow configuration for CI/CD.

## 🛠 Installation
- 🎯 Prerequisites
- Python 3.10
- Git
- Docker Desktop (optional, for Docker execution)
- Jupyter Notebook (optional, for notebook execution)
- NVIDIA Drivers supporting CUDA 12.1 (for GPU acceleration)


### 🔧 Installation Methods
Choose the option that best fits your operating system and preferences.

#### 📄 Option 1: Using the Batch Script (Windows Only)
Run the Batch Script

- Double-click on Run_Interactive-GGUF-Visualization-Tool.bat and follow the on-screen prompts to install dependencies, set up the environment, and operate every aspect of the program seamlessly!

#### 🖥️ Option 2: Manual Installation
Clone the Repository

````
git clone https://github.com/BenevolenceMessiah/Interactive-GGUF-Visualization-Tool.git
cd Interactive-GGUF-Visualization-Tool
````

Set Up a Virtual Environment

````
python -m venv .venv
````

Activate the Virtual Environment

Windows:
````
.venv\Scripts\activate
````

Unix/Linux:
````
source .venv/bin/activate
````

Upgrade Pip and Install Dependencies

````
pip install --upgrade pip
pip install -r requirements.txt
Clone and Install llama-cpp-python
````

````
git clone https://github.com/ggerganov/llama-cpp-python.git
cd llama-cpp-python
LLAMA_CUBLAS=1 pip install .
cd ..
````

Build Documentation (Optional)

````
cd docs
mkdocs build
cd ..
````

Launch the Gradio Interface

````
python main.py
````

Run via Docker (Optional)

````
docker build -t gguf-visualization-tool .
docker run -d -p 7934:7934 gguf-visualization-tool
````

Launch the Jupyter Notebook (Optional)

````
jupyter notebook interactive_gguf_visualization_tool.ipynb
````
## 🧪 Testing
Ensuring the reliability and robustness of the Interactive GGUF Visualization Tool is paramount. Follow these steps to run comprehensive tests:


### Run Unit Tests

````
python -m unittest discover tests
Purpose: Validates the functionality of individual components within the application.
Execute Jupyter Notebook Tests
````

Open and run all cells in interactive_gguf_visualization_tool.ipynb to ensure notebook-based interactions function correctly.
Docker Container Testing

Build Docker Image:
````
docker build -t gguf-visualization-tool .
````

Run Docker Container:
````
docker run --gpus all -d -p 7934:7934 --name gguf_test_container gguf-visualization-tool
````

Verify Gradio Server:
````
curl -sSf http://localhost:7934 || exit 1
````

Cleanup:
````
docker stop gguf_test_container
docker rm gguf_test_container
````

## 📝 Usage
Once installed, you can access the Interactive GGUF Visualization Tool through various interfaces:

Gradio Web UI: Access via `http://localhost:7933` (default port).
Docker Container: Access via `http://localhost:7934`.
📓 Jupyter Notebook: Interact directly through interactive_gguf_visualization_tool.ipynb.
🌐 Using Gradio Web UI
Launch Gradio:

````
python main.py
````
Interact with the Interface:


Model Overview: Load and manage GGUF models.
Inference: Chat with your model.
Visualization: Explore various visualizations of your model's architecture and behaviors.
Self-Awareness Experiment: Conduct AI self-reflection experiments.
Run Tests: Execute unit tests directly from the interface.
🐳 Using Docker
Build and Run Docker Container:

````
docker build -t gguf-visualization-tool .
docker run -d -p 7934:7934 gguf-visualization-tool
````

## Access the Application:

Navigate to `http://localhost:7934` in your web browser.

📓 Using Jupyter Notebook
Launch Jupyter Notebook:

````
jupyter notebook interactive_gguf_visualization_tool.ipynb
````

Interact with the Notebook:


Execute cells to load models, run inference, and visualize data within the notebook environment.

## 🔧 Configuration
Customize your experience by adjusting parameters and settings:

Context Length (n_ctx): Modify the context window size for model inference.
GPU Layers (n_gpu_layers): Allocate specific layers to GPU processing for optimized performance.
CPU Threads (n_threads): Define the number of CPU threads for model computations.
These configurations can be adjusted through the Gradio interface or by modifying the relevant scripts.

### ✅ Additional Notes
CUDA Support: Ensure that your system has NVIDIA drivers supporting CUDA 12.1 installed for GPU acceleration.
Ports Configuration:
Gradio: Runs on port 7933 by default.
Docker Container: Runs on port 7934.
These can operate simultaneously without port conflicts.
Batch Script: The Run_Interactive-GGUF-Visualization-Tool.bat script simplifies installation and execution on Windows systems, managing audio playback and environment setup.

## 📝 To Do
We're committed to continuously enhancing the Interactive GGUF Visualization Tool. Here's what's on the horizon:

🌐 Google Colab Integration:
Develop a Google Colab Notebook to leverage T4 GPUs, enabling cloud-based model training and inference.
🤖 HuggingFace Spaces Deployment:
Create a HuggingFace Space to harness free architectures, expanding accessibility and user reach.
📊 Enhanced Visualization Techniques:
Integrate advanced visualization methods to provide deeper insights into model behaviors and structures.
📈 Performance Optimizations:
Optimize backend processes for faster inference and smoother user interactions.
🔒 Security Enhancements:
Implement robust security measures to protect user data and model integrity.
🧑‍🤝‍🧑 Community Contributions:
Open the project to community contributions, fostering collaborative development and feature expansions.
📚 Comprehensive Documentation:
Expand the docs/ directory with detailed guides, tutorials, and API references to assist users in maximizing the tool's potential.
Your feedback and contributions are invaluable! If you have suggestions, feature requests, or would like to contribute, please reach out or submit a pull request.

### 🛡 License
This project is licensed under the MIT License.

### 📬 Contact
For any inquiries, support, or collaboration opportunities, please contact[Benevolence Messiah](https://huggingface.co/BenevolenceMessiah).

---
