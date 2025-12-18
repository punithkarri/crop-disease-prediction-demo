import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="AI Crop Disease Prediction", layout="centered")

st.title("🌱 AI-Driven Crop Disease Prediction System")
st.write("Demo version – model integration placeholder")

uploaded_file = st.file_uploader("Upload leaf image", ["jpg", "jpeg", "png"])

CLASS_NAMES = [
    "Healthy Leaf",
    "Early Blight",
    "Late Blight",
    "Leaf Spot",
    "Powdery Mildew"
]

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, use_column_width=True)

    # Demo prediction (random for UI demo)
    disease = np.random.choice(CLASS_NAMES)
    confidence = np.random.uniform(0.7, 0.95)

    st.success(f"Detected Disease: {disease}")
    st.info(f"Confidence: {confidence*100:.2f}%")
    st.warning("10-Day Risk (Estimated): Medium")

st.markdown("---")
st.caption("Prototype UI for AI-Based Crop Disease Prediction")
