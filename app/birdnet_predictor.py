from birdnet_analyzer import analyze
from pathlib import Path
import pandas as pd
import uuid

OUTPUT_FOLDER = Path("birdnet_results")
OUTPUT_FOLDER.mkdir(exist_ok=True)


def predict_bird(audio_path):

    run_folder = OUTPUT_FOLDER / str(uuid.uuid4())
    run_folder.mkdir(exist_ok=True)

    analyze(
        audio_input=str(audio_path),
        output=str(run_folder),
        top_n=5,
        min_conf=0.20
    )

    txt_files = list(
        run_folder.glob("*.BirdNET.selection.table.txt")
    )

    if len(txt_files) == 0:
        return None

    df = pd.read_csv(
        txt_files[0],
        sep="\t"
    )

    if df.empty:
        return None

    best = df.sort_values(
        by="Confidence",
        ascending=False
    ).iloc[0]

    return {

        "species": best["Common Name"],

        "speciesCode": best["Species Code"],

        "confidence": round(
            float(best["Confidence"]) * 100,
            2
        ),

        "category": "Bird"

    }