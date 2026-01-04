"""
Deepfake Detection Platform - Streamlit App
Auteur : Thiané DIA
Licence : MIT
"""

import streamlit as st
from detectors.ensemble import analyze_media
from utils.report_generator import generate_pdf_report
from utils.video_utils import extract_frames
import tempfile
import cv2
from PIL import Image

st.set_page_config(
    page_title="Deepfake Detection Platform",
    layout="wide"
)

st.title("Deepfake Detection Platform")

uploaded_file = st.file_uploader(
    "Uploader une image ou une vidéo",
    type=["jpg", "png", "mp4"]
)



if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    if uploaded_file.type.startswith("video"):
        st.info("Vidéo détectée. Extraction frames...")
        frames = extract_frames(file_path)
        st.write(f"{len(frames)} frames extraites, analyse en cours...")
        results = []
        for f in frames:
            results.append(analyze_media(f))
        avg_score = sum([r["score"] for r in results]) / len(results)
        verdict = "Deepfake suspecté" if avg_score > 0.5 else "Authentique probable"
        st.metric("Probabilité Deepfake moyenne", f"{int(avg_score*100)}%")
        st.write("### Détails par frame")
        for i, r in enumerate(results):
            st.write(f"Frame {i}: {r['verdict']} - Score: {r['score']}")
            st.image(r["heatmap"], channels="BGR", width=300)
        if st.button("📄 Générer rapport PDF"):
            pdf_path = generate_pdf_report(results[0])  # PDF basé sur 1ère frame + heatmap
            with open(pdf_path, "rb") as f:
                st.download_button("Télécharger le rapport", f, file_name="deepfake_report.pdf")
    else:
        st.info("Image détectée. Analyse en cours...")
        result = analyze_media(file_path)
        st.metric("Probabilité Deepfake", f"{int(result['score']*100)}%")
        st.write("### Résultats par détecteur")
        st.json(result["details"])
        st.image(result["heatmap"], channels="BGR", width=400)
        if st.button("📄 Générer le rapport PDF"):
            pdf_path = generate_pdf_report(result)
            with open(pdf_path, "rb") as f:
                st.download_button("Télécharger le rapport", f, file_name="deepfake_report.pdf")

















































