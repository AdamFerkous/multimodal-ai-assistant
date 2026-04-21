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
        model="black-forest-labs/FLUX.1-schnell",
        token=token,
        provider="hf-inference"
    )

    image = client.text_to_image(prompt)
    return image
