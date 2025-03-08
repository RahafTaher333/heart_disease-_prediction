import streamlit as st
import pickle

# Load the trained model (assume the model is saved in a file named heart_disease_model.pkl)
heart_disease_model = pickle.load(open('heart_disease_model.pkl', 'rb'))

# Title of the project
st.title("Heart Disease Prediction App")

# Section for inputs
st.header("Enter Patient Information")

# Input: Age (in years)
age = st.number_input("Enter age (in years, must be positive)", min_value=1)

# Input: Sex (1 = Male, 0 = Female)
sex = st.selectbox(
    "Enter sex (1 = Male, 0 = Female)",
    options=[0, 1]
)
st.write("Please select 1 for Male and 0 for Female.")  # Explanation for sex input

# Input: Chest pain type (0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic)
cp = st.selectbox(
    "Enter chest pain type:",
    options=[0, 1, 2, 3]
)
st.write("0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic.")  # Explanation for chest pain

# Input: Resting blood pressure (trestbps)
trestbps = st.number_input("Enter resting blood pressure (e.g., 130 mmHg)", min_value=1)

# Input: Cholesterol level (chol)
chol = st.number_input("Enter cholesterol level (e.g., 220 mg/dl)", min_value=1)

# Input: Fasting blood sugar (1 = > 120 mg/dl, 0 = <= 120 mg/dl)
fbs = st.selectbox(
    "Enter fasting blood sugar (1 = > 120 mg/dl, 0 = <= 120 mg/dl)",
    options=[0, 1]
)
st.write("1 = Fasting Blood Sugar > 120 mg/dl, 0 = Fasting Blood Sugar <= 120 mg/dl.")  # Explanation for fasting blood sugar

# Input: Resting electrocardiographic results (restecg)
restecg = st.selectbox(
    "Enter resting electrocardiographic results:",
    options=[0, 1, 2]
)
st.write("0 = Normal, 1 = ST-T Wave Abnormality, 2 = Left Ventricular Hypertrophy.")  # Explanation for electrocardiographic results

# Input: Maximum heart rate achieved (thalach)
thalach = st.number_input("Enter maximum heart rate achieved (e.g., 150 bpm)", min_value=1)

# Input: Exercise-induced angina (1 = Yes, 0 = No)
exang = st.selectbox(
    "Enter exercise-induced angina (1 = Yes, 0 = No)",
    options=[0, 1]
)
st.write("1 = Exercise-induced Angina, 0 = No Exercise-induced Angina.")  # Explanation for exercise-induced angina

# Input: ST depression induced by exercise relative to rest (oldpeak)
oldpeak = st.number_input("Enter ST depression induced by exercise relative to rest", min_value=0.0, step=0.1)

# Input: Slope of the peak exercise ST segment (slope)
slope = st.selectbox(
    "Enter slope of the ST segment during exercise:",
    options=[0, 1, 2]
)
st.write("0 = Upsloping, 1 = Flat, 2 = Downsloping.")  # Explanation for slope

# Input: Number of major coronary arteries with obstruction (ca)
ca = st.selectbox(
    "Enter number of major coronary arteries with obstruction:",
    options=[0, 1, 2]
)
st.write("0 = No obstruction, 1 = One artery obstructed, 2 = Two arteries obstructed.")  # Explanation for coronary arteries

# Input: Thalassemia type (thal)
thal = st.selectbox(
    "Enter thalassemia type:",
    options=[1, 2, 3]
)
st.write("1 = Normal, 2 = Fixed Defect, 3 = Reversable Defect.")  # Explanation for thalassemia type

# Section for prediction results
st.header("Prediction Result")

# Button for showing the result
if st.button("Show Result"):
    # Prepare input data to match the model's expected input format
    input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    
    # Predict using the trained model
    prediction = heart_disease_model.predict(input_data)
    
    # If the prediction is 1, it means the person has heart disease
    if prediction[0] == 1:
        st.error("The person has heart disease.")
    else:
        st.success("The person does not have heart disease.")

