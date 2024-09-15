# gradio_app.py

import gradio as gr
import os
import webbrowser
import subprocess
from modules.gguf_model import GGUFModel
import modules.data_utils as data_utils
import modules.visualization_utils as visualization_utils
from modules.self_awareness_experiment import run_self_referential_question
from modules.download_tool import search_models, download_model  # Import from download_tool.py
from modules.visualization_tool import get_visualization_data  # Import from visualization_tool.py
import torch

# Global variable for the model
gguf_model = None

def load_model(model_name, n_ctx, n_gpu_layers, n_threads):
    global gguf_model
    model_path = os.path.join('models', model_name)
    gguf_model = GGUFModel(model_path, n_ctx=n_ctx, n_gpu_layers=n_gpu_layers, n_threads=n_threads)
    try:
        gguf_model.load_model()
        device = "CUDA" if torch.cuda.is_available() else "CPU"
        return f"Model '{model_name}' loaded successfully on {device}."
    except Exception as e:
        return f"Error loading model: {e}"

def unload_model():
    global gguf_model
    if gguf_model:
        gguf_model.unload_model()
        return "Model unloaded successfully."
    else:
        return "No model is currently loaded."

def generate_response(prompt, history):
    if gguf_model:
        response = gguf_model.generate(prompt)
        # Save chat to outputs
        data_utils.save_chat(prompt, response)
        # Update chat history
        history = history + [(prompt, response)]
        return history, ""
    else:
        return history, "Please load a model first."

def run_tests():
    # Run unit tests and return the results
    result = subprocess.run(["python", "-m", "unittest", "discover", "tests"], capture_output=True, text=True)
    return result.stdout + result.stderr

def open_huggingface_repo():
    url = "https://huggingface.co/spaces/BenevolenceMessiah/gguf-my-repo-2"
    webbrowser.open_new_tab(url)
    return "Opened HuggingFace repository in a new tab."

def search_huggingface_models(query):
    model_names = search_models(query)
    return gr.Dropdown.update(choices=model_names)

def download_huggingface_model(model_id):
    status = download_model(model_id)
    return status

def refresh_models():
    model_files = []
    for root, dirs, files in os.walk('models'):
        for file in files:
            if file.endswith('.gguf') or file.endswith('.bin'):
                relative_path = os.path.relpath(os.path.join(root, file), 'models')
                model_files.append(relative_path)
        for dir in dirs:
            model_files.append(dir)
    return gr.Dropdown.update(choices=model_files)

def get_previous_chats():
    data_utils.ensure_directory_exists('outputs')
    chat_files = os.listdir('outputs')
    json_files = [f for f in chat_files if f.endswith('.json')]
    return json_files

def load_chat(chat_file):
    chat_data = data_utils.load_chat(chat_file)
    history = []
    if 'prompt' in chat_data and 'response' in chat_data:
        history.append((chat_data['prompt'], chat_data['response']))
    return history

def run_self_awareness_experiment(prompt):
    from modules.self_awareness_experiment import run_self_referential_question
    if gguf_model:
        return run_self_referential_question(gguf_model, prompt)
    else:
        return "Please load a model first."

def get_visualization_json():
    if gguf_model:
        # Example: Get attention weights or other data for visualization
        # This is a placeholder; implement actual data retrieval as needed
        visualization_data = get_visualization_data(gguf_model)
        return visualization_data
    else:
        return {}

# Define Gradio Interface
def create_gradio_interface():
    with gr.Blocks(css=".gradio-container {background-color: #f0f0f0;}") as demo:
        with gr.Tabs():
            with gr.TabItem("Model Overview"):
                gr.Markdown("# Model Overview")
                # Model loading components
                model_dropdown = gr.Dropdown(choices=refresh_models().choices, label="Select Model")
                n_ctx_slider = gr.Slider(256, 4096, value=512, step=64, label="Context Length")
                n_gpu_layers_slider = gr.Slider(0, 40, value=0, step=1, label="GPU Layers")
                n_threads_slider = gr.Slider(1, os.cpu_count(), value=4, step=1, label="CPU Threads")
                load_button = gr.Button("Load Model")
                unload_button = gr.Button("Unload Model")
                load_status = gr.Textbox(label="Status", interactive=False, lines=2)

                # Actions
                load_button.click(
                    load_model,
                    inputs=[model_dropdown, n_ctx_slider, n_gpu_layers_slider, n_threads_slider],
                    outputs=load_status
                )
                unload_button.click(unload_model, outputs=load_status)

                # Model search components
                gr.Markdown("## Search and Download Models from HuggingFace")
                search_bar = gr.Textbox(label="Search GGUF Models on HuggingFace", placeholder="Enter model name...")
                search_button = gr.Button("Search")
                search_results = gr.Dropdown(label="Search Results", choices=[])
                download_button = gr.Button("Download Model")
                refresh_button = gr.Button("Refresh Models")
                open_repo_button = gr.Button("Open GGUF Repository")

                search_button.click(search_huggingface_models, inputs=search_bar, outputs=search_results)
                download_button.click(download_huggingface_model, inputs=search_results, outputs=load_status)
                refresh_button.click(refresh_models, outputs=model_dropdown)
                open_repo_button.click(open_huggingface_repo)

            with gr.TabItem("Inference"):
                gr.Markdown("# Inference")
                with gr.Row():
                    load_chat_dropdown = gr.Dropdown(choices=get_previous_chats(), label="Load Previous Chat")
                    load_chat_button = gr.Button("Load Chat")
                    new_chat_button = gr.Button("New Chat")

                chat_history = gr.Chatbot()
                user_input = gr.Textbox(placeholder="Type your message here...", lines=2)
                send_button = gr.Button("Send")

                # Actions
                send_button.click(
                    generate_response,
                    inputs=[user_input, chat_history],
                    outputs=[chat_history, user_input]
                )

                load_chat_button.click(
                    load_chat,
                    inputs=load_chat_dropdown,
                    outputs=chat_history
                )

                new_chat_button.click(
                    lambda: ([], ""),
                    inputs=None,
                    outputs=[chat_history, user_input]
                )

            with gr.TabItem("Visualization"):
                gr.Markdown("# Visualization")
                with gr.Tabs():
                    with gr.TabItem("Layer Visualization"):
                        gr.Markdown("### Layer Visualization")
                        layer_vis = gr.HTML("<div id='layer-visualization'></div>")
                        # Fetch visualization data and embed D3.js script
                        layer_data = gr.State()

                        def update_layer_visualization():
                            data = get_visualization_json()
                            return data

                        layer_data_event = gr.Button("Load Layer Visualization Data")
                        layer_data_event.click(update_layer_visualization, outputs=layer_data)

                        # Embed D3.js script with the visualization data
                        layer_vis_content = gr.HTML("""
                        <script src="https://d3js.org/d3.v7.min.js"></script>
                        <div id="visualization"></div>
                        <script>
                            const data = {data_json};

                            // Example D3.js visualization
                            const width = 800;
                            const height = 600;

                            const svg = d3.select("#visualization")
                                          .append("svg")
                                          .attr("width", width)
                                          .attr("height", height);

                            // Simple scatter plot example
                            svg.selectAll("circle")
                               .data(data.input.concat(data.output))
                               .enter()
                               .append("circle")
                               .attr("cx", d => d.x * 10)
                               .attr("cy", d => height - d.y)
                               .attr("r", 5)
                               .attr("fill", d => d.z === 0 ? "blue" : "red");
                        </script>
                        """)
                        
                        # Bind the data to the HTML component
                        layer_data_event.click(
                            lambda data: layer_vis_content.replace("{data_json}", json.dumps(data)),
                            inputs=layer_data,
                            outputs=layer_vis
                        )

                    with gr.TabItem("Attention Visualization"):
                        gr.Markdown("### Attention Visualization")
                        attention_vis = gr.HTML("<div id='attention-visualization'></div>")
                        # Similar implementation as Layer Visualization
                        attention_data = gr.State()

                        def update_attention_visualization():
                            data = get_visualization_json()  # Modify as per actual attention data
                            return data

                        attention_data_event = gr.Button("Load Attention Visualization Data")
                        attention_data_event.click(update_attention_visualization, outputs=attention_data)

                        attention_vis_content = gr.HTML("""
                        <script src="https://d3js.org/d3.v7.min.js"></script>
                        <div id="attention-visualization"></div>
                        <script>
                            const data = {data_json};

                            // Example D3.js visualization for attention
                            const width = 800;
                            const height = 600;

                            const svg = d3.select("#attention-visualization")
                                          .append("svg")
                                          .attr("width", width)
                                          .attr("height", height);

                            // Simple heatmap example
                            const heatmapData = data.attention || [];

                            const colorScale = d3.scaleSequential(d3.interpolateBlues)
                                                 .domain([0, d3.max(heatmapData.flat())]);

                            const cellSize = 20;

                            svg.selectAll("rect")
                               .data(heatmapData.flat())
                               .enter()
                               .append("rect")
                               .attr("x", (d, i) => (i % 30) * cellSize)
                               .attr("y", (d, i) => Math.floor(i / 30) * cellSize)
                               .attr("width", cellSize)
                               .attr("height", cellSize)
                               .attr("fill", d => colorScale(d));
                        </script>
                        """)

                        # Bind the data to the HTML component
                        attention_data_event.click(
                            lambda data: attention_vis_content.replace("{data_json}", json.dumps(data)),
                            inputs=attention_data,
                            outputs=attention_vis
                        )

                    with gr.TabItem("Weight Visualization"):
                        gr.Markdown("### Weight Visualization")
                        weight_vis = gr.HTML("<div id='weight-visualization'></div>")
                        # Similar implementation as above
                        weight_data = gr.State()

                        def update_weight_visualization():
                            data = get_visualization_json()  # Modify as per actual weight data
                            return data

                        weight_data_event = gr.Button("Load Weight Visualization Data")
                        weight_data_event.click(update_weight_visualization, outputs=weight_data)

                        weight_vis_content = gr.HTML("""
                        <script src="https://d3js.org/d3.v7.min.js"></script>
                        <div id="weight-visualization"></div>
                        <script>
                            const data = {data_json};

                            // Example D3.js visualization for weights
                            const width = 800;
                            const height = 600;

                            const svg = d3.select("#weight-visualization")
                                          .append("svg")
                                          .attr("width", width)
                                          .attr("height", height);

                            // Simple bar chart example
                            const weights = data.weights || [];

                            const xScale = d3.scaleBand()
                                             .domain(d3.range(weights.length))
                                             .range([0, width])
                                             .padding(0.1);

                            const yScale = d3.scaleLinear()
                                             .domain([0, d3.max(weights)])
                                             .range([height, 0]);

                            svg.selectAll("rect")
                               .data(weights)
                               .enter()
                               .append("rect")
                               .attr("x", (d, i) => xScale(i))
                               .attr("y", d => yScale(d))
                               .attr("width", xScale.bandwidth())
                               .attr("height", d => height - yScale(d))
                               .attr("fill", "steelblue");
                        </script>
                        """)

                        # Bind the data to the HTML component
                        weight_data_event.click(
                            lambda data: weight_vis_content.replace("{data_json}", json.dumps(data)),
                            inputs=weight_data,
                            outputs=weight_vis
                        )

                    with gr.TabItem("Node Embedding Visualization"):
                        gr.Markdown("### Node Embedding Visualization")
                        embedding_vis = gr.HTML("<div id='embedding-visualization'></div>")
                        # Similar implementation as above
                        embedding_data = gr.State()

                        def update_embedding_visualization():
                            data = get_visualization_json()  # Modify as per actual embedding data
                            return data

                        embedding_data_event = gr.Button("Load Embedding Visualization Data")
                        embedding_data_event.click(update_embedding_visualization, outputs=embedding_data)

                        embedding_vis_content = gr.HTML("""
                        <script src="https://d3js.org/d3.v7.min.js"></script>
                        <div id="embedding-visualization"></div>
                        <script>
                            const data = {data_json};

                            // Example D3.js visualization for node embeddings
                            const width = 800;
                            const height = 600;

                            const svg = d3.select("#embedding-visualization")
                                          .append("svg")
                                          .attr("width", width)
                                          .attr("height", height);

                            // Assuming embeddings are 3D coordinates
                            const embeddings = data.embeddings || [];

                            const projection = d3.geoOrthographic()
                                                 .translate([width / 2, height / 2])
                                                 .scale(200);

                            svg.selectAll("circle")
                               .data(embeddings)
                               .enter()
                               .append("circle")
                               .attr("cx", d => d[0] * 10 + width / 2)
                               .attr("cy", d => -d[1] * 10 + height / 2)
                               .attr("r", 5)
                               .attr("fill", "green");
                        </script>
                        """)

                        # Bind the data to the HTML component
                        embedding_data_event.click(
                            lambda data: embedding_vis_content.replace("{data_json}", json.dumps(data)),
                            inputs=embedding_data,
                            outputs=embedding_vis
                        )

            with gr.TabItem("Self-Awareness Experiment"):
                gr.Markdown("# Self-Awareness Experiment")
                experiment_prompt = gr.Textbox(placeholder="Ask a self-referential question...", lines=2)
                experiment_button = gr.Button("Run Experiment")
                experiment_output = gr.Textbox(label="Experiment Output", interactive=False, lines=5)

                experiment_button.click(
                    run_self_awareness_experiment,
                    inputs=experiment_prompt,
                    outputs=experiment_output
                )

            with gr.TabItem("Run Tests"):
                gr.Markdown("# Run Unit Tests")
                test_output = gr.Textbox(label="Test Output", interactive=False, lines=15)
                run_tests_button = gr.Button("Run Tests")

                run_tests_button.click(
                    run_tests,
                    outputs=test_output
                )

        return demo
