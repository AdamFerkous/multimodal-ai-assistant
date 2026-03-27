import streamlit as st
from text_generation import generate_text
from sentiment_analysis import analyze_sentiment
from image_generation import generate_image
from speech_generation import generate_speech

st.set_page_config(page_title="Assistant Multimodal IA", layout="centered")

st.title("Assistant de création de contenu multimodal")

theme = st.text_input("Entrez un thème (ex : nature zen, ville futuriste)")

if st.button("Générer"):
    if theme:
        with st.spinner("Génération en cours..."):
            st.session_state.text = generate_text(theme)
            st.session_state.sentiment = analyze_sentiment(st.session_state.text)
            st.session_state.image = generate_image(theme)
    else:
        st.warning("Veuillez entrer un thème.")

if "text" in st.session_state:

    st.subheader("Texte généré")
    st.write(st.session_state.text)

    if st.button("Écouter la description"):
        audio_file = generate_speech(st.session_state.text)
        st.audio(audio_file)

    st.subheader("Image générée")
    st.image(st.session_state.image)

    st.subheader("Analyse de sentiment")
    st.write(st.session_state.sentiment)
