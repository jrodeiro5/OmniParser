import gradio as gr
from omnitool.screen_parser import ScreenParser
from PIL import Image
import numpy as np
import cv2

parser = ScreenParser()

def process_image(input_image):
    # Convert Gradio image to numpy array if necessary
    if isinstance(input_image, Image.Image):
        input_image = np.array(input_image)
    
    # Ensure BGR format for OpenCV
    if len(input_image.shape) == 3 and input_image.shape[2] == 3:
        input_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2BGR)
    
    # Process image using OmniParser
    try:
        result = parser.parse_screen(input_image)
        return result
    except Exception as e:
        return f"Error processing image: {str(e)}"

# Create Gradio interface
demo = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Text(),
    title="OmniParser Demo",
    description="Upload a screenshot to analyze UI elements"
)

if __name__ == "__main__":
    demo.launch()