{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d59ac2b1-9cb6-48f4-bbec-ff7663dcd9c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import pandas as pd\n",
    "\n",
    "# Load model\n",
    "model = joblib.load('news_classifier.pkl')\n",
    "\n",
    "# Class mapping\n",
    "class_map = {\n",
    "    0: \"World\",\n",
    "    1: \"Sports\",\n",
    "    2: \"Business\",\n",
    "    3: \"Science/Tech\"\n",
    "}\n",
    "\n",
    "st.title(\"📰 News Article Classifier\")\n",
    "st.markdown(\"Classify articles into: World, Sports, Business, or Science/Tech\")\n",
    "\n",
    "# Input options\n",
    "tab1, tab2 = st.tabs([\"Text Input\", \"File Upload\"])\n",
    "\n",
    "with tab1:\n",
    "    text = st.text_area(\"Enter article text:\", height=200)\n",
    "    if st.button(\"Classify\"):\n",
    "        if text:\n",
    "            prediction = model.predict([text])[0]\n",
    "            st.success(f\"Predicted Category: **{class_map[prediction]}**\")\n",
    "        else:\n",
    "            st.warning(\"Please enter some text\")\n",
    "\n",
    "with tab2:\n",
    "    file = st.file_uploader(\"Upload text file\", type=[\"txt\"])\n",
    "    if file:\n",
    "        text = file.read().decode(\"utf-8\")\n",
    "        st.text_area(\"File Content\", text, height=200)\n",
    "        if st.button(\"Classify File\"):\n",
    "            prediction = model.predict([text])[0]\n",
    "            st.success(f\"Predicted Category: **{class_map[prediction]}**\")\n",
    "\n",
    "st.markdown(\"---\")\n",
    "st.write(\"Model Accuracy: 91.2% (Linear SVM)\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
