import streamlit as st
import requests
import csv 
def main():
   
    st.title('Model Prediction')

    
    age = st.number_input('Age', min_value=0, max_value=120, value=30)
    gender = st.radio('Gender', ['Male', 'Female'])
    marital_status = st.radio('Marital Status', ['Single', 'Married'])
    occupation = st.number_input('Occupation', min_value=1, max_value=4, value=2)
    monthly_income = st.number_input('Monthly Income', min_value=0, value=50000)
    educational_qualifications = st.number_input('Occupation', min_value=1, max_value=5, value=2)
    family_size = st.number_input('Family Size', min_value=1,max_value=6, value=1)
    feedback = st.number_input('Feedback', min_value=0,max_value=1, value=1)

   
    def make_prediction(age, gender, marital_status, occupation, monthly_income, educational_qualifications, family_size, feedback):
        data = {
            'Age': age,
            'Gender': 1 if gender == 'Female' else 0,
            'Marital_Status': 1 if marital_status == 'Married' else 0,
            'Occupation': occupation,
            'Monthly_Income': monthly_income,
            'Educational_Qualifications': educational_qualifications,
            'Family_size': family_size,
            'Feedback': feedback
        }
        response = requests.post('http://localhost:8000/predict', json=data)
        if response.status_code == 200:
            prediction = response.json()['prediction']
            return prediction
        else:
            st.error('Error: Unable to get prediction from server')

  
    if st.button('Predict'):
        prediction = make_prediction(age, gender, marital_status, occupation, monthly_income, educational_qualifications, family_size, feedback)
        if prediction is not None:
          
            input_data = [age, gender, marital_status, occupation, monthly_income, educational_qualifications, family_size, feedback, prediction]
            with open('input_data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(input_data)
            st.success(f'Prediction: {prediction}')

if __name__ == "__main__":
    main()
