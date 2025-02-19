import streamlit as st
import joblib
import re

# Load the trained model and vectorizer
log_reg = joblib.load("logistic_model.pkl")
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Preprocessing function
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W+', ' ', text)  # Remove special characters
    return text

# Streamlit UI
st.title("📰 Fake News Detector")
st.write("Enter a news article below, and the model will predict whether it's **Fake** or **Real**.")

# User input
user_input = st.text_area("✍️ Paste a news article here:", "")

if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("⚠ Please enter some text to analyze.")
    else:
        # Preprocess and vectorize the input
        cleaned_text = clean_text(user_input)
        text_tfidf = tfidf_vectorizer.transform([cleaned_text])

        # Make a prediction
        prediction = log_reg.predict(text_tfidf)[0]
        result = "🟢 Real News" if prediction == 1 else "🔴 Fake News"

        # Display result
        st.subheader(f"Prediction: {result}")