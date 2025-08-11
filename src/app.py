from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

with open("src/model/model.pkl", "rb") as f:
    model = pickle.load(f)

class Features(BaseModel):
    features: list[list[float]]  # Accepts multiple samples

@app.get("/")
def read_root():
    return {"message": "ML Model API"}

@app.post("/predict")
def predict(data: Features):
    # Convert to numpy array for batch prediction
    features_array = np.array(data.features)
    prediction = model.predict(features_array)
    return {"prediction": prediction.tolist()}