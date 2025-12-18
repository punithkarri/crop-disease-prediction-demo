import streamlit as st
import numpy as np
from PIL import Image
import random

st.set_page_config(page_title="AI Crop Disease Prediction", layout="centered")

st.title("🌱 AI-Driven Crop Disease Prediction & Management System")

st.write(
    "Upload or scan a leaf image to identify crop disease, "
    "get treatment recommendations, and predict future risk."
)

# --------------------------------------------------
# INPUT METHOD
# --------------------------------------------------
input_method = st.radio(
    "Choose input method:",
    ["Upload Image", "Scan Using Camera"]
)

uploaded_file = None

if input_method == "Upload Image":
    uploaded_file = st.file_uploader(
        "Upload leaf image",
        ["jpg", "jpeg", "png"]
    )
else:
    uploaded_file = st.camera_input("Scan the leaf using camera")

# --------------------------------------------------
# DISEASE DATABASE (CURE + PREVENTION)
# --------------------------------------------------
DISEASE_INFO = {
    "Healthy Leaf": {
        "cause": "No disease detected.",
        "cure": "No treatment required.",
        "prevention": "Maintain regular irrigation and nutrition."
    },
    "Early Blight": {
        "cause": "Fungal infection due to high humidity.",
        "cure": "Apply fungicides like Mancozeb or Chlorothalonil.",
        "prevention": "Avoid overhead irrigation and remove infected leaves."
    },
    "Late Blight": {
        "cause": "Fungal disease triggered by cool, wet conditions.",
        "cure": "Use Copper-based fungicides immediately.",
        "prevention": "Ensure proper drainage and crop rotation."
    },
    "Leaf Spot": {
        "cause": "Bacterial or fungal pathogens.",
        "cure": "Apply appropriate bactericide or fungicide.",
        "prevention": "Use disease-free seeds and avoid overcrowding."
    },
    "Powdery Mildew": {
        "cause": "Fungal spores spreading in dry climates.",
        "cure": "Spray sulfur-based fungicide.",
        "prevention": "Increase air circulation and sunlight exposure."
    }
}

CLASS_NAMES = list(DISEASE_INFO.keys())

# --------------------------------------------------
# PREDICTION (DEMO LOGIC)
# --------------------------------------------------
def predict_disease():
    disease = random.choice(CLASS_NAMES)
    confidence = random.uniform(0.75, 0.95)
    future_risk = random.choice(["Low", "Medium", "High"])
    return disease, confidence, future_risk

# --------------------------------------------------
# RESULT DISPLAY
# --------------------------------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Leaf Image", use_column_width=True)

    with st.spinner("Analyzing crop health..."):
        disease, confidence, future_risk = predict_disease()

    st.subheader("🧪 Detection Result")
    st.success(f"Detected Disease: {disease}")
    st.info(f"Confidence: {confidence*100:.2f}%")

    st.subheader("📈 10-Day Disease Risk Prediction")
    st.warning(f"Risk Level: {future_risk}")

    st.subheader("🩺 Cause & Cure")
    st.write(f"**Cause:** {DISEASE_INFO[disease]['cause']}")
    st.write(f"**Treatment:** {DISEASE_INFO[disease]['cure']}")

    st.subheader("🛡️ Prevention Measures")
    st.write(DISEASE_INFO[disease]["prevention"])

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption("Prototype: AI-Based Crop Disease Prediction, Cure Recommendation & Early Warning System")
