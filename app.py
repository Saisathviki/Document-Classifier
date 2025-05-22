import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('news_classifier.pkl')

# Class mapping
class_map = {
    0: "World",
    1: "Sports",
    2: "Business",
    3: "Science/Tech"
}

st.title("📰 News Article Classifier")
st.markdown("Classify articles into: World, Sports, Business, or Science/Tech")

# Input options
tab1, tab2 = st.tabs(["Text Input", "File Upload"])

with tab1:
    text = st.text_area("Enter article text:", height=200)
    if st.button("Classify"):
        if text:
            prediction = model.predict([text])[0]
            st.success(f"Predicted Category: **{class_map[prediction]}**")
        else:
            st.warning("Please enter some text")

with tab2:
    file = st.file_uploader("Upload text file", type=["txt"])
    if file:
        text = file.read().decode("utf-8")
        st.text_area("File Content", text, height=200)
        if st.button("Classify File"):
            prediction = model.predict([text])[0]
            st.success(f"Predicted Category: **{class_map[prediction]}**")

st.markdown("---")
st.write("Model Accuracy: 91.2% (Linear SVM)")
