# Multimodal AI Content Assistant

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![AI](https://img.shields.io/badge/AI-Multimodal-green)

## Description

A web application that generates creative text, images, and sentiment analysis from a given theme using AI models.  
It also includes text-to-speech functionality to listen to the generated content.


## Features

- Generate creative text from a user-defined theme
- Generate images using Stable Diffusion
- Perform sentiment analysis on generated text
- Convert text to speech (audio playback)
- Interactive web interface built with Streamlit

## Project Structure

```
multimodal-ai-assistant/
├── app.py
├── text_generation.py
├── image_generation.py
├── sentiment_analysis.py
├── speech_generation.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.9 or higher


## Technologies

- Python  
- Streamlit (web interface)  
- Hugging Face Transformers (text generation & sentiment analysis)  
- Stable Diffusion XL via Hugging Face (image generation)  
- gTTS (Google Text-to-Speech)  


## Installation (Terminal)

python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  


## Configuration of Hugging Face Token

This project uses the Hugging Face API for image generation.

1. Create an account on https://huggingface.co  
2. Generate an access token  
3. Create a `.env` file at the root of the project  
4. Add the following line:

HF_TOKEN=YOUR_HUGGINGFACE_TOKEN


## Run the application

streamlit run app.py


## Usage

Enter a theme in the interface, then click "Generate" to obtain:

- a creative text  
- an AI-generated image  
- a sentiment analysis  
- the ability to listen to the generated description (text-to-speech)  


## Author

Adam Ferkous  
AI & Data Student
