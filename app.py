import streamlit as st
import joblib

# Load the pre-trained model
model = joblib.load("model.joblib")

# Streamlit UI
st.title("Sentiment Analysis App")
st.write("Enter a sentence and the model will predict whether it's positive or negative.")

# Text input from user
text_input = st.text_input("Your sentence:")

# When user enters a sentence
if text_input:
    prediction = model.predict([text_input])[0]
    label = "😊 Positive" if prediction == 1 else "😠 Negative"
    st.success(f"Predicted Sentiment: {label}")