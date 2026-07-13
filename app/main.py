from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import shutil

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
async def upload_image(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return JSONResponse(
        {
            "message": "Image uploaded successfully",
            "filename": file.filename,
            "path": file_path
        }
    )