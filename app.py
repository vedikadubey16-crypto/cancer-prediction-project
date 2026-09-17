
import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("Cancer Cell Prediction")

st.write("Enter the values:")

# 30 features
mean_radius = st.number_input("Mean Radius")
mean_texture = st.number_input("Mean Texture")
mean_perimeter = st.number_input("Mean Perimeter")
mean_area = st.number_input("Mean Area")
mean_smoothness = st.number_input("Mean Smoothness")
mean_compactness = st.number_input("Mean Compactness")
mean_concavity = st.number_input("Mean Concavity")
mean_concave_points = st.number_input("Mean Concave Points")
mean_symmetry = st.number_input("Mean Symmetry")
mean_fractal_dimension = st.number_input("Mean Fractal Dimension")

radius_error = st.number_input("Radius Error")
texture_error = st.number_input("Texture Error")
perimeter_error = st.number_input("Perimeter Error")
area_error = st.number_input("Area Error")
smoothness_error = st.number_input("Smoothness Error")
compactness_error = st.number_input("Compactness Error")
concavity_error = st.number_input("Concavity Error")
concave_points_error = st.number_input("Concave Points Error")
symmetry_error = st.number_input("Symmetry Error")
fractal_dimension_error = st.number_input("Fractal Dimension Error")

worst_radius = st.number_input("Worst Radius")
worst_texture = st.number_input("Worst Texture")
worst_perimeter = st.number_input("Worst Perimeter")
worst_area = st.number_input("Worst Area")
worst_smoothness = st.number_input("Worst Smoothness")
worst_compactness = st.number_input("Worst Compactness")
worst_concavity = st.number_input("Worst Concavity")
worst_concave_points = st.number_input("Worst Concave Points")
worst_symmetry = st.number_input("Worst Symmetry")
worst_fractal_dimension = st.number_input("Worst Fractal Dimension")


if st.button("Predict"):

    data = {
        "mean radius": mean_radius,
        "mean texture": mean_texture,
        "mean perimeter": mean_perimeter,
        "mean area": mean_area,
        "mean smoothness": mean_smoothness,
        "mean compactness": mean_compactness,
        "mean concavity": mean_concavity,
        "mean concave points": mean_concave_points,
        "mean symmetry": mean_symmetry,
        "mean fractal dimension": mean_fractal_dimension,

        "radius error": radius_error,
        "texture error": texture_error,
        "perimeter error": perimeter_error,
        "area error": area_error,
        "smoothness error": smoothness_error,
        "compactness error": compactness_error,
        "concavity error": concavity_error,
        "concave points error": concave_points_error,
        "symmetry error": symmetry_error,
        "fractal dimension error": fractal_dimension_error,

        "worst radius": worst_radius,
        "worst texture": worst_texture,
        "worst perimeter": worst_perimeter,
        "worst area": worst_area,
        "worst smoothness": worst_smoothness,
        "worst compactness": worst_compactness,
        "worst concavity": worst_concavity,
        "worst concave points": worst_concave_points,
        "worst symmetry": worst_symmetry,
        "worst fractal dimension": worst_fractal_dimension
    }

    response = requests.post(
    f"{API_URL}/predict",
    json=data
    )

    if response.status_code == 200:

        result = response.json()

        st.success("Prediction: " + result["result"])

        st.write(
            "Cancer Probability:",
            result["cancer_probability"] * 100,
            "%"
        )

    else:

        st.error("Prediction failed")

        st.write("Status Code:", response.status_code)

        st.write("Backend Response:", response.text)