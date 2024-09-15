# main.py

from gradio_app import create_gradio_interface

def main():
    demo = create_gradio_interface()
    demo.queue()  # Enable request queueing
    demo.launch(server_name="0.0.0.0", server_port=7933, share=False)

if __name__ == "__main__":
    main()
