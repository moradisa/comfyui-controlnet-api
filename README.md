# comfyui-controlnet-api

This project implements a RESTful API using FastAPI that integrates ControlNet with Stable Diffusion for image and video generation. Users can upload files, which are processed by the models, and retrieve the generated outputs.



## Setup

### Prerequisites
- Python 3.8+


### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/moradisa/comfyui-controlnet-api.git
    cd comfyui-controlnet-api
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. Download the Stable Diffusion and ControlNet models:
    - [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/blob/main/sd-v1-4.ckpt)
    - [ControlNet](https://huggingface.co/lllyasviel/ControlNet/blob/main/models/control_sd15_openpose.pth)

4. Place the models in the following directories:
    ```
    models/StableDiffusion/
    models/ControlNet/
    ```
### Usage

1. **Start the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload
    ```

2. **Process a file:**
    - **POST /process/**: Upload an image or video file.
    - **GET /output/{filename}**: Retrieve the generated output file.

### Example Requests

- **Using `curl`:**
    ```bash
    # Upload and process a file
    curl -X POST "http://127.0.0.1:8000/process/" -F "file=@input_file.mp4"

    # Retrieve the generated file
    curl -X GET "http://127.0.0.1:8000/output/generated_video.mp4" -o output_video.mp4
    ```

