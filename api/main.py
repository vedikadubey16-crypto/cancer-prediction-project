from fastapi import FastAPI
from pydantic import BaseModel,Field
import joblib
import pandas as pd
app = FastAPI()
model = joblib.load("models/final_model.pkl")
class CancerInput(BaseModel):
    mean_radius: float = Field(alias="mean radius")
    mean_texture: float = Field(alias="mean texture")
    mean_perimeter: float = Field(alias="mean perimeter")
    mean_area: float = Field(alias="mean area")
    mean_smoothness: float = Field(alias="mean smoothness")
    mean_compactness: float = Field(alias="mean compactness")
    mean_concavity: float = Field(alias="mean concavity")
    mean_concave_points: float = Field(alias="mean concave points")
    mean_symmetry: float = Field(alias="mean symmetry")
    mean_fractal_dimension: float = Field(alias="mean fractal dimension")

    radius_error: float = Field(alias="radius error")
    texture_error: float = Field(alias="texture error")
    perimeter_error: float = Field(alias="perimeter error")
    area_error: float = Field(alias="area error")
    smoothness_error: float = Field(alias="smoothness error")
    compactness_error: float = Field(alias="compactness error")
    concavity_error: float = Field(alias="concavity error")
    concave_points_error: float = Field(alias="concave points error")
    symmetry_error: float = Field(alias="symmetry error")
    fractal_dimension_error: float = Field(alias="fractal dimension error")

    worst_radius: float = Field(alias="worst radius")
    worst_texture: float = Field(alias="worst texture")
    worst_perimeter: float = Field(alias="worst perimeter")
    worst_area: float = Field(alias="worst area")
    worst_smoothness: float = Field(alias="worst smoothness")
    worst_compactness: float = Field(alias="worst compactness")
    worst_concavity: float = Field(alias="worst concavity")
    worst_concave_points: float = Field(alias="worst concave points")
    worst_symmetry: float = Field(alias="worst symmetry")
    worst_fractal_dimension: float = Field(alias="worst fractal dimension")
@app.get("/")
def home():
    return {
        "message": "Cancer Prediction API is running"
    }
@app.post("/predict")
def predict(data: CancerInput):

        data = data.model_dump(by_alias=True)

        df = pd.DataFrame([data])

        prediction = model.predict(df)[0]

        cancer_probability = model.predict_proba(df)[0][1]

        if prediction == 1:
            result = "Malignant"
        else:
            result = "Benign"

        return {
            "prediction": int(prediction),
            "result": result,
            "cancer_probability": float(cancer_probability)
        }

    
