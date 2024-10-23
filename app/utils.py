import cv2
import torch
from PIL import Image
import numpy as np

def preprocess_input(input_path):
    # Preprocess the input file, handle images and videos.

    if input_path.endswith(('.jpg', '.jpeg', '.png')):
        # Load and preprocess an image
        image = Image.open(input_path)
        image = image.resize((512, 512))
        image = np.array(image) / 255.0
        input_tensor = torch.tensor(image).permute(2, 0, 1).unsqueeze(0)
        return input_tensor
    elif input_path.endswith('.mp4'):
        # Handle video frames, resize to 512x512, and stack them
        cap = cv2.VideoCapture(input_path)
        frames = []
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (512, 512))
            frame = frame.astype(np.float32) / 255.0
            frames.append(torch.tensor(frame).permute(2, 0, 1).unsqueeze(0))
        cap.release()
        return torch.stack(frames)
    else:
        raise ValueError("Unsupported file format")

def save_output(output_image, output_path):
    # Save output image to disk.
    output_image = (output_image * 255).cpu().numpy().astype(np.uint8)
    img = Image.fromarray(output_image)
    img.save(output_path)

