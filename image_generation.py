from huggingface_hub import InferenceClient
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

def generate_image(prompt):
    token = os.getenv("HF_TOKEN")
    if not token:
        raise RuntimeError("HF_TOKEN non défini")

    client = InferenceClient(
        model="stabilityai/stable-diffusion-xl-base-1.0",
        token=token,
        provider="hf-inference"
    )

    image = client.text_to_image(prompt)
    return image
