# 📰 Fake News Detection using Machine Learning

## 📌 Project Overview
This project implements a **Fake News Detection** model using **Natural Language Processing (NLP)** and **Machine Learning**. The goal is to classify news articles as **fake (0)** or **real (1)** based on their textual content.

## 🚀 Features
✅ Preprocesses text data using **NLTK** (tokenization, stopword removal, lemmatization).  
✅ Converts text into numerical features using **TF-IDF Vectorization**.  
✅ Trains a **Logistic Regression** model for classification.  
✅ Evaluates performance using **accuracy, classification report, and confusion matrix**.  
✅ Deploys the model as a **Streamlit web application**.  

## 📂 Dataset
The dataset consists of two CSV files:
- `fake.csv` → Contains fake news articles (labeled as **0**).
- `true.csv` → Contains real news articles (labeled as **1**).

## 🔧 Installation & Setup
To set up the environment and run the project, follow these steps:

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Streamlit Web App**
```bash
streamlit run app.py
```

## 📊 Model Training & Evaluation
1. Load and preprocess the dataset.
2. Convert text into TF-IDF vectors.
3. Split the data into training and testing sets.
4. Train a **Logistic Regression** model.
5. Evaluate performance using:
   - **Accuracy**
   - **Classification Report**
   - **Confusion Matrix**

## 🎯 Deployment
The model is deployed using **Streamlit**, allowing users to enter a news article and receive a **real or fake prediction**.

## 📌 Future Enhancements
🚀 Improve accuracy by testing other models (e.g., **Random Forest, XGBoost**).  
🚀 Implement **deep learning models** like **BERT** for improved NLP capabilities.  
🚀 Deploy as an **API** using Flask or FastAPI.  

## 🤝 Contributing
Pull requests are welcome! If you find an issue or want to contribute, please open a PR.

## 📜 License
This project is **MIT Licensed**. Feel free to use and modify it as needed.
