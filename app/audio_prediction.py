from app.birdnet_predictor import predict_bird


def predict_audio(audio_path):
    """
    Predict bird species using BirdNET Analyzer.
    """

    result = predict_bird(audio_path)

    if result is None:
        return {
            "status": "FAILED",
            "species": "Unknown",
            "confidence": 0,
            "category": "Unknown",
            "soundType": "Unknown",
            "conservationStatus": "Unknown",
            "environmentNoise": "Unknown",
            "noiseFiltered": False,
            "model": "BirdNET Analyzer"
        }

    return {
        "status": "SUCCESS",

        "species": result["species"],

        "speciesCode": result["speciesCode"],

        "confidence": result["confidence"],

        "category": "Bird",

        "soundType": "Bird Call",

        # Placeholder values for now
        "conservationStatus": "Protected",

        "environmentNoise": "Low",

        "noiseFiltered": True,

        "model": "BirdNET Analyzer"
    }