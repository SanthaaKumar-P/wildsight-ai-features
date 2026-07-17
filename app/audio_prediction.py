from birdnetlib import Recording
from app.birdnet_loader import analyzer


def predict_audio(audio_path):

    recording = Recording(
        analyzer,
        str(audio_path)
    )

    recording.analyze()

    if len(recording.detections) == 0:

        return {
            "status": "FAILED",
            "predictedSpecies": "Unknown",
            "confidence": 0,
            "model": "BirdNET"
        }

    best = max(
        recording.detections,
        key=lambda x: x["confidence"]
    )

    return {
        "status": "SUCCESS",
        "predictedSpecies": best["common_name"],
        "scientificName": best["scientific_name"],
        "confidence": round(best["confidence"] * 100, 2),
        "model": "BirdNET"
    }