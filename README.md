# Assistant de création de contenu multimodal

## Prérequis
- Python 3.9 ou supérieur

## Description
Application web permettant de générer un texte créatif, une image et une analyse de sentiment à partir d’un thème.

## Technologies
- Python
- Streamlit (interface web)
- Hugging Face Transformers (génération de texte et analyse de sentiment)
- Stable Diffusion XL via Hugging Face (génération d’images)
- gTTS (Google Text-to-Speech)

## Installation (dans le terminal)
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  

## Configuration du token Hugging Face

Ce projet utilise l’API Hugging Face pour la génération d’images.

1. Créer un compte sur https://huggingface.co
2. Générer un token d’accès
3. Créer un fichier `.env` à la racine du projet
4. Ajouter la ligne suivante :

HF_TOKEN=VOTRE_TOKEN_HUGGINGFACE


## Lancement
streamlit run app.py

## Utilisation
Entrer un thème dans l’interface, puis cliquer sur "Générer" pour obtenir :
- un texte créatif
- une image générée par IA
- une analyse de sentiment
- la possibilité d’écouter la description générée (synthèse vocale)
