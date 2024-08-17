import gradio as gr

# Define a simple function that returns a string
def get_message():
    return "Hello, world!"

# Set up the Gradio interface using this function
interface = gr.Interface(
    fn=get_message,  # Pass the function itself, not calling it
    inputs=[],  # No inputs required for this function
    outputs="text",  # The output is text, as the function returns a string
    title="Simple String Return Example",
    description="Click the button to get a message."
)

# Launch the interface
interface.launch()
