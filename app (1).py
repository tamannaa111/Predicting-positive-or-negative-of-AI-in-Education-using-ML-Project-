import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the feature names and their corresponding abbreviations
feature_names = {
    'CM': 'How comfortable are you using AI tools for learning or teaching?',
    'TS': 'Do AI tools save time in completing assignments or preparing lessons?',
    'EN': 'Have AI tools increased your engagement with the learning material?',
    'VC': 'Are you challenged to verify the accuracy of AI-generated data?',
    'IC': 'Do you think AI tools reduce critical thinking or creativity?',
    'OR': 'Do you feel over-reliant on AI tools for educational tasks?',
    'PC': 'Privacy concerns:',
    'NI': 'Have you experienced any negative impacts from AI on your learning or teaching process?',
    'EF': 'How effective are AI tools with your personal learning needs?',
    'IN': 'Have AI tools increased your interest in learning new topics?',
}

# Create the Streamlit app
st.title('AI in Education Prediction App')

# Get user input for features
input_data = []
for feature_abbr, feature_question in feature_names.items():
    value = st.slider(feature_question, 0, 4, 2)  # Assuming values are between 0 and 4
    input_data.append(value)

# Create a DataFrame for input data
input_df = pd.DataFrame([input_data], columns=feature_names.keys())

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_df)[0]

    # Display the prediction
    if prediction == 0:
        st.write('Prediction: **Negative**')
    else:
        st.write('Prediction: **Positive**')