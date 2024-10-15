import gradio as gr
from rembg import remove
import numpy as np
from PIL import Image

def remove_background(input_image):
    # Convert the input image to a format suitable for rembg
    output_image = remove(input_image)
    return output_image

# Create Gradio interface
iface = gr.Interface(
    fn=remove_background,
    inputs=gr.Image(type="numpy", label="Upload Image"),
    outputs=gr.Image(label="Image without Background"),
    title="Background Remover",
    description="Upload an image to remove its background."
)

iface.launch()
