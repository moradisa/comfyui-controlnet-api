import torch
from diffusers import StableDiffusionPipeline, ControlNetModel
from .utils import preprocess_input, save_output

class ComfyUIModel:
    def __init__(self):
        self.device = "cpu"

        # Load the ControlNet model from the ControlNet directory
        self.controlnet = ControlNetModel.from_pretrained(
            "models/ControlNet/"
        ).to(self.device)

        # Load the Stable Diffusion model with mismatched size handling
        self.pipeline = StableDiffusionPipeline.from_pretrained(
            "models/StableDiffusion/",
            controlnet=self.controlnet,
            low_cpu_mem_usage=False,        # Memory usage flag
            ignore_mismatched_sizes=True    # Ignore weight size mismatch
        ).to(self.device)
    
    def process(self, input_path, output_path):
        input_data = preprocess_input(input_path)  # Load and preprocess input data
        
        # Run inference
        with torch.no_grad():
            result = self.pipeline(input_data)

        # Save the output result
        save_output(result.images[0], output_path)
