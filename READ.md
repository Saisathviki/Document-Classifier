# 📰 News Article Classifier

This project is a machine learning web application that classifies news articles into one of four categories: **World**, **Sports**, **Business**, or **Science/Tech**. It uses the [AG News dataset](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset) and is built with **Scikit-learn**, **Streamlit**, and **Python**.

---

## 🚀 Demo

Run it locally and see how it classifies news in real-time!

---

## 🧠 Model Information

- **Dataset:** [AG News (Kaggle)](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset)
- **Best Model:** Linear SVM (TF-IDF + LinearSVC)
- **Accuracy:** 91.2% on test data
- **Vectorization:** TF-IDF with unigrams and bigrams
- **Model File:** `news_classifier.pkl`

---

## 📁 Project Structure

news-classifier/
├── ag_news/ # Folder containing train.csv and test.csv
├── app.py # Streamlit app
├── modeltraining.py # Model training & export script
├── datapreparation.py # Data preprocessing and model testing
├── news_classifier.pkl # Trained classifier pipeline
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 💻 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/news-classifier.git
cd news-classifier
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Linux/Mac
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Run the Streamlit App

```bash
streamlit run app.py
```
#### 📦 Required Files:

news_classifier.pkl: Trained model (produced using modeltraining.py)

ag_news/train.csv and ag_news/test.csv: Dataset files from AG News

app.py: Streamlit frontend

#### ✨ Features
🔍 Classify manually typed or uploaded text files

📊 Trained with multiple models (Naive Bayes, Logistic Regression, SVM)

🎯 Real-time prediction with model accuracy

📈 Visualizations of model performance and class distribution

#### 🛠️ Tech Stack
Frontend: Streamlit

Backend/ML: Python, Scikit-learn, Pandas, Seaborn

Model Export: joblib

#### ✅ To-Do
 Add support for multilingual news articles

 Deploy on HuggingFace or Streamlit Cloud

 Add charts for model interpretability (e.g., SHAP)

#### 📝 License
MIT License. Feel free to use, modify, and distribute.









