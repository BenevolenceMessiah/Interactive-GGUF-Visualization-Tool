# main.py

import torch
import gradio as gr
from modules.gguf_model import GGUFModel  # Adjust the import based on your project structure
# Import other necessary modules

def get_device():
    """Detects if CUDA is available and returns the appropriate device."""
    if torch.cuda.is_available():
        print("CUDA is available. Using GPU.")
        return torch.device("cuda")
    else:
        print("CUDA is not available. Falling back to CPU.")
        return torch.device("cpu")

def main():
    try:
        # Initialize device
        device = get_device()

        # Load the GGUF model with the detected device
        model = GGUFModel(
            model_path='models/your_model.gguf',  # Replace with your actual model path
            device=device,
            n_ctx=2048,
            n_gpu_layers=40 if device.type == 'cuda' else 0,
            n_threads=8
        )
        model.load_model()

        # Define Gradio interface
        with gr.Blocks() as demo:
            gr.Markdown("# Interactive GGUF Visualization Tool")

            with gr.Tab("Model Overview"):
                # Add UI components for model overview
                load_model_button = gr.Button("Load Model")
                download_model_button = gr.Button("Download from HuggingFace")

            with gr.Tab("Inference"):
                # Add UI components for inference
                chatbot = gr.Chatbot()
                with gr.Row():
                    user_input = gr.Textbox(show_label=False, placeholder="Enter your message here...")
                    submit_button = gr.Button("Send")

            with gr.Tab("Visualization"):
                # Add UI components for visualization
                gr.Markdown("## 3D Brain Visualization")
                # Embed the 3D visualization using HTML or other components

            with gr.Tab("Self-Awareness Experiment"):
                # Add UI components for self-awareness experiments
                experiment_input = gr.Textbox(label="Your Experiment Prompt", placeholder="Ask your AI about self-awareness...")
                experiment_output = gr.Textbox(label="AI Response")

            with gr.Tab("Unit Tests"):
                # Add UI components to run unit tests
                run_tests_button = gr.Button("Run Unit Tests")
                test_results = gr.Textbox(label="Test Results")

            with gr.Tab("Audio Integration"):
                # Add UI components for audio feedback
                play_audio_button = gr.Button("Play Audio")

        # Define interaction functions
        def handle_chat(user_message):
            try:
                response = model.generate(prompt=user_message)
                return response
            except Exception as e:
                return f"An error occurred during inference: {e}"

        def run_tests():
            try:
                import unittest
                loader = unittest.TestLoader()
                tests = loader.discover('tests')
                test_runner = unittest.TextTestRunner(verbosity=2)
                result = test_runner.run(tests)
                if result.wasSuccessful():
                    return "All tests passed successfully!"
                else:
                    return "Some tests failed. Check logs for details."
            except Exception as e:
                return f"An error occurred while running tests: {e}"

        def play_audio():
            try:
                # Implement audio playback logic
                return "Playing audio..."
            except Exception as e:
                return f"An error occurred while playing audio: {e}"

        # Link UI components to functions
        submit_button.click(handle_chat, inputs=user_input, outputs=chatbot)
        run_tests_button.click(run_tests, inputs=None, outputs=test_results)
        play_audio_button.click(play_audio, inputs=None, outputs=None)

        # Launch Gradio server
        demo.launch(server_name="0.0.0.0", server_port=7933)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Optionally, log the error to a file or monitoring service

if __name__ == "__main__":
    main()
