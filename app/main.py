# WROOM Technical Assessment 2, web API

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from .model import ComfyUIModel
import os

app = FastAPI()

# Load the model at startup
comfyui_model = ComfyUIModel()

# Upload image or video file to process
@app.post("/process/")
async def process_file(file: UploadFile = File(...)):
    input_path = f"input/{file.filename}"
    output_path = f"output/{file.filename}"
    
    # Save the uploaded file to input folder
    with open(input_path, "wb") as buffer:
        buffer.write(await file.read())

    # Generate the output using the ControlNet model
    comfyui_model.process(input_path, output_path)
    
    return {"output_file": output_path}

# Endpoint to get the generated output
@app.get("/output/{filename}")
async def get_output(filename: str):
    file_path = f"output/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}

