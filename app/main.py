from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import shutil

from app.prediction import predict_species

app = FastAPI(
    title="WildSight AI Service",
    description="AI Powered Wildlife Species Recognition API",
    version="1.0.0"
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Welcome to WildSight AI",
        "status": "Running",
        "service": "Wildlife Image Recognition"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "tensorflow": "Loaded",
        "ready": True
    }


@app.post("/predict-image")
async def predict_image(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prediction = predict_species(file_path)

    return JSONResponse(
        {
            "status": "SUCCESS",
            "predictedSpecies": prediction["species"].title(),
            "confidence": prediction["confidence"],
            "model": "MobileNetV2"
        }
    )