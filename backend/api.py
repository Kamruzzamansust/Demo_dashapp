from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the saved model
model = joblib.load(r"./random_forest_model.pkl")

# Define the FastAPI app
app = FastAPI()


class PredictionRequest(BaseModel):
    Age: int
    Gender: int
    Marital_Status: int
    Occupation: int
    Monthly_Income: int
    Educational_Qualifications: int
    Family_size: int
    Feedback: int


@app.post("/predict")
async def predict(data: PredictionRequest):
    
    input_data = pd.DataFrame([data.dict()])

    # Rename the columns to match the training data
    input_data = input_data.rename(columns={
        "Monthly_Income": "Monthly Income",
        "Educational_Qualifications": "Educational Qualifications",
        "Family_size": "Family size",
        "Marital_Status": "Marital Status"
    })

   
    prediction = model.predict(input_data)

    # Return the prediction
    return {"prediction": prediction[0]}


@app.get("/")
async def read_root():
    return {"message": "Welcome to the model prediction API!"}
